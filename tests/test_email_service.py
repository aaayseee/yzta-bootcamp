import os
import unittest
from unittest.mock import MagicMock, patch

from services.email_service import send_password_reset_email


class EmailServiceTests(unittest.TestCase):
    @patch("services.email_service.smtplib.SMTP")
    def test_reset_email_contains_tokenized_link(self, smtp_class):
        smtp = MagicMock()
        smtp_class.return_value.__enter__.return_value = smtp
        environment = {
            "SMTP_HOST": "smtp.test.local",
            "SMTP_PORT": "587",
            "SMTP_USER": "smtp-user",
            "SMTP_PASSWORD": "smtp-password",
            "SMTP_FROM": "LoyalCart <no-reply@test.local>",
            "SMTP_USE_TLS": "1",
            "LOYALCART_APP_URL": "https://loyalcart.test",
        }
        with patch.dict(os.environ, environment, clear=False):
            sent = send_password_reset_email("admin@test.local", "reset-token")

        self.assertTrue(sent)
        smtp.starttls.assert_called_once()
        smtp.login.assert_called_once_with("smtp-user", "smtp-password")
        message = smtp.send_message.call_args.args[0]
        self.assertIn(
            "https://loyalcart.test/?reset_token=reset-token",
            message.get_content(),
        )


if __name__ == "__main__":
    unittest.main()
