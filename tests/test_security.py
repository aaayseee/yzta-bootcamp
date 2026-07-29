import os
import tempfile
import unittest
from unittest.mock import patch

from db.repository import authenticate_user, initialize_database
from db.security import (
    create_password_reset_token,
    initialize_security_tables,
    list_integration_events,
    record_integration_event,
    reset_password,
)


class SecurityWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.environment = patch.dict(
            os.environ,
            {
                "DB_ENGINE": "sqlite",
                "SQLITE_PATH": os.path.join(self.temp_dir.name, "security.db"),
                "LOYALCART_ADMIN_USERNAME": "admin",
                "LOYALCART_ADMIN_EMAIL": "admin@test.local",
                "LOYALCART_ADMIN_PASSWORD": "OldStrongPassword1!",
            },
            clear=False,
        )
        self.environment.start()
        initialize_database()
        initialize_security_tables()

    def tearDown(self):
        self.environment.stop()
        self.temp_dir.cleanup()

    def test_reset_token_is_single_use(self):
        request = create_password_reset_token("admin")
        self.assertIsNotNone(request)
        token, email = request
        self.assertEqual(email, "admin@test.local")

        self.assertTrue(reset_password(token, "NewStrongPassword1!"))
        self.assertIsNotNone(authenticate_user("admin", "NewStrongPassword1!"))
        self.assertIsNone(authenticate_user("admin", "OldStrongPassword1!"))
        self.assertFalse(reset_password(token, "AnotherPassword1!"))

    def test_integration_events_are_persistent(self):
        event_id = record_integration_event(
            "telegram", "connection_test", "success", "message_id=42", "admin"
        )
        events = list_integration_events()
        self.assertEqual(events[0]["id"], event_id)
        self.assertEqual(events[0]["provider"], "telegram")
        self.assertEqual(events[0]["status"], "success")


if __name__ == "__main__":
    unittest.main()
