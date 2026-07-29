import os
import tempfile
import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from main import app


PAYLOAD = {
    "Tenure": 4.0,
    "PreferredLoginDevice": "Mobile Phone",
    "CityTier": 1,
    "WarehouseToHome": 15.0,
    "PreferredPaymentMode": "Debit Card",
    "Gender": "Female",
    "HourSpendOnApp": 3.0,
    "NumberOfDeviceRegistered": 3,
    "PreferedOrderCat": "Laptop & Accessory",
    "SatisfactionScore": 2,
    "MaritalStatus": "Single",
    "NumberOfAddress": 2,
    "Complain": 1,
    "OrderAmountHikeFromlastYear": 15.0,
    "CouponUsed": 1,
    "OrderCount": 2,
    "DaySinceLastOrder": 12.0,
    "CashbackAmount": 160.0,
    "CustomerId": "API-TEST-1",
    "CreatedBy": "admin",
}


class ApiTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.environment = patch.dict(
            os.environ,
            {
                "DB_ENGINE": "sqlite",
                "SQLITE_PATH": os.path.join(self.temp_dir.name, "api.db"),
                "LOYALCART_ADMIN_PASSWORD": "StrongAdminPassword1!",
                "LOYALCART_API_KEY": "test-api-key",
            },
            clear=False,
        )
        self.environment.start()
        self.client_context = TestClient(app)
        self.client = self.client_context.__enter__()

    def tearDown(self):
        self.client_context.__exit__(None, None, None)
        self.environment.stop()
        self.temp_dir.cleanup()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "ok")

    def test_prediction_requires_key_and_is_persisted(self):
        unauthorized = self.client.post("/predict", json=PAYLOAD)
        self.assertEqual(unauthorized.status_code, 401)

        response = self.client.post(
            "/predict",
            json=PAYLOAD,
            headers={"X-API-Key": "test-api-key"},
        )
        self.assertEqual(response.status_code, 200)
        body = response.json()
        self.assertIn(body["churn_prediction"], (0, 1))
        self.assertTrue(body["database_saved"])
        self.assertIsInstance(body["prediction_id"], int)


if __name__ == "__main__":
    unittest.main()
