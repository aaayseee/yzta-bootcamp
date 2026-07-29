import os
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from db.repository import (
    DuplicateUserError,
    authenticate_user,
    clear_predictions,
    create_user,
    initialize_database,
    list_predictions,
    save_prediction,
)


class RepositoryTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test.db")
        self.environment = patch.dict(
            os.environ,
            {
                "DB_ENGINE": "sqlite",
                "SQLITE_PATH": self.db_path,
                "LOYALCART_ADMIN_USERNAME": "admin",
                "LOYALCART_ADMIN_EMAIL": "admin@test.local",
                "LOYALCART_ADMIN_PASSWORD": "StrongAdminPassword1!",
            },
            clear=False,
        )
        self.environment.start()
        initialize_database()

    def tearDown(self):
        self.environment.stop()
        self.temp_dir.cleanup()

    def test_admin_password_is_hashed_and_authenticates(self):
        user = authenticate_user("admin", "StrongAdminPassword1!")
        self.assertEqual(user["role"], "administrator")

        connection = sqlite3.connect(self.db_path)
        row = connection.execute(
            "SELECT password_hash FROM users WHERE username = 'admin'"
        ).fetchone()
        connection.close()
        self.assertTrue(row[0].startswith("pbkdf2_sha256$"))
        self.assertNotIn("StrongAdminPassword1!", row[0])

    def test_user_creation_and_duplicate_protection(self):
        create_user("manager1", "manager1@test.local", "StrongPassword1!")
        self.assertIsNotNone(authenticate_user("manager1", "StrongPassword1!"))
        self.assertIsNone(authenticate_user("manager1", "wrong-password"))
        with self.assertRaises(DuplicateUserError):
            create_user("manager1", "other@test.local", "StrongPassword2!")

    def test_prediction_history_round_trip(self):
        prediction_id = save_prediction(
            customer_id="CUSTOMER-1",
            features={"Tenure": 4, "Complain": 1},
            prediction=1,
            probability=0.82,
            model_version="test-model",
            result="Terk Riski Var",
            action="Müşteriyi arayın",
            source="test",
            created_by="admin",
        )
        rows = list_predictions()
        self.assertEqual(rows[0]["id"], prediction_id)
        self.assertEqual(rows[0]["customer_id"], "CUSTOMER-1")
        self.assertAlmostEqual(rows[0]["probability"], 0.82)

        clear_predictions()
        self.assertEqual(list_predictions(), [])


if __name__ == "__main__":
    unittest.main()
