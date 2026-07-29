"""Telegram Bot API client."""

from typing import Any, Dict

import requests


class TelegramError(RuntimeError):
    pass


def send_telegram_message(
    bot_token: str,
    chat_id: str,
    message: str,
    timeout: int = 10,
    http_client=requests,
) -> Dict[str, Any]:
    if not bot_token or not chat_id:
        raise TelegramError("Telegram tokenı ve chat ID zorunludur.")
    response = http_client.post(
        f"https://api.telegram.org/bot{bot_token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": message,
            "disable_web_page_preview": True,
        },
        timeout=timeout,
    )
    try:
        payload = response.json()
    except ValueError as exc:
        raise TelegramError("Telegram geçersiz bir yanıt döndürdü.") from exc
    if response.status_code != 200 or not payload.get("ok"):
        description = payload.get("description", f"HTTP {response.status_code}")
        raise TelegramError(f"Telegram mesajı gönderilemedi: {description}")
    return payload

