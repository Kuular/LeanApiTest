import uuid

LEANTECH_URL = "https://sandbox.leantech.me/customers/v1/"
random_user = f"test_user_{uuid.uuid4()}"


def get_create_customer_payload(app_user_id: str) -> dict:
    return {"app_user_id": app_user_id}


def get_headers(lean_app_token: str) -> dict:
    headers = {
        "accept": "application/json",
        "lean-app-token": lean_app_token
    }
    return headers
