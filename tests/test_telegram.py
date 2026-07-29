import unittest

from services.telegram import TelegramError, send_telegram_message


class FakeResponse:
    def __init__(self, status_code, payload):
        self.status_code = status_code
        self.payload = payload

    def json(self):
        return self.payload


class FakeHttpClient:
    def __init__(self, response):
        self.response = response
        self.calls = []

    def post(self, url, json, timeout):
        self.calls.append({"url": url, "json": json, "timeout": timeout})
        return self.response


class TelegramTests(unittest.TestCase):
    def test_successful_message_uses_real_bot_endpoint_shape(self):
        client = FakeHttpClient(
            FakeResponse(200, {"ok": True, "result": {"message_id": 42}})
        )
        result = send_telegram_message(
            "secret-token", "-100123", "test message", http_client=client
        )
        self.assertTrue(result["ok"])
        self.assertEqual(
            client.calls[0]["url"],
            "https://api.telegram.org/botsecret-token/sendMessage",
        )
        self.assertEqual(client.calls[0]["json"]["chat_id"], "-100123")

    def test_provider_error_is_not_reported_as_success(self):
        client = FakeHttpClient(
            FakeResponse(401, {"ok": False, "description": "Unauthorized"})
        )
        with self.assertRaisesRegex(TelegramError, "Unauthorized"):
            send_telegram_message(
                "bad-token", "-100123", "test message", http_client=client
            )


if __name__ == "__main__":
    unittest.main()
