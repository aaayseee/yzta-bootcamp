"""SMTP email helper for password reset messages."""

import os
import smtplib
from email.message import EmailMessage
from urllib.parse import urlencode


def smtp_is_configured() -> bool:
    return all(
        os.getenv(name)
        for name in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD", "SMTP_FROM")
    )


def send_password_reset_email(recipient: str, token: str) -> bool:
    if not smtp_is_configured():
        return False
    app_url = os.getenv("LOYALCART_APP_URL", "http://localhost:8501").rstrip("/")
    reset_url = f"{app_url}/?{urlencode({'reset_token': token})}"
    message = EmailMessage()
    message["Subject"] = "LoyalCart şifre sıfırlama"
    message["From"] = os.environ["SMTP_FROM"]
    message["To"] = recipient
    message.set_content(
        "Şifrenizi 30 dakika içinde aşağıdaki bağlantıdan sıfırlayabilirsiniz:\n\n"
        f"{reset_url}\n\nBu talebi siz oluşturmadıysanız mesajı yok sayın."
    )

    host = os.environ["SMTP_HOST"]
    port = int(os.getenv("SMTP_PORT", "587"))
    use_tls = os.getenv("SMTP_USE_TLS", "1") == "1"
    with smtplib.SMTP(host, port, timeout=15) as smtp:
        if use_tls:
            smtp.starttls()
        smtp.login(os.environ["SMTP_USER"], os.environ["SMTP_PASSWORD"])
        smtp.send_message(message)
    return True
