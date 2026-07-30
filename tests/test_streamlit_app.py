import os
import unittest
from pathlib import Path
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


class StreamlitSmokeTests(unittest.TestCase):
    def setUp(self):
        self.db_path = Path("loyalcart_streamlit_test.db").resolve()
        self.db_path.unlink(missing_ok=True)
        self.environment = patch.dict(
            os.environ,
            {
                "DB_ENGINE": "sqlite",
                "SQLITE_PATH": str(self.db_path),
                "LOYALCART_ADMIN_PASSWORD": "StrongAdminPassword1!",
            },
            clear=False,
        )
        self.environment.start()

    def tearDown(self):
        self.environment.stop()
        self.db_path.unlink(missing_ok=True)

    def test_login_and_all_pages_render_without_errors(self):
        app = AppTest.from_file("arayuz.py").run(timeout=30)
        self.assertEqual(list(app.exception), [])
        self.assertEqual(list(app.error), [])

        app.text_input[0].set_value("admin")
        app.text_input[1].set_value("StrongAdminPassword1!")
        app.button[0].click().run(timeout=30)
        self.assertTrue(app.session_state["logged_in"])

        for option in list(app.radio[0].options):
            app.radio[0].set_value(option).run(timeout=30)
            self.assertEqual(
                list(app.exception), [], f"{option} sayfasında exception oluştu"
            )
            self.assertEqual(list(app.error), [], f"{option} sayfasında hata oluştu")

    def test_empty_login_shows_validation_message(self):
        app = AppTest.from_file("arayuz.py").run(timeout=30)

        app.button[0].click().run(timeout=30)

        self.assertEqual(list(app.exception), [])
        self.assertEqual(len(app.error), 1)
        self.assertEqual(
            app.error[0].value,
            "Lütfen kullanıcı adı ve şifre alanlarını doldurun.",
        )


if __name__ == "__main__":
    unittest.main()
