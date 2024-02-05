from typing import Optional, Any

import allure
import requests

from data import random_user, LEANTECH_URL, get_create_customer_payload, get_headers


def create_customer(lean_app_token: str, app_user_id: str = random_user) -> tuple[Optional[Any], Optional[Any]]:
    with allure.step(f"Create Customer with {app_user_id=}"):
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "lean-app-token": lean_app_token
        }
        response = requests.post(url=LEANTECH_URL, json=get_create_customer_payload(app_user_id),
                                 headers=headers).json()
        customer_id = response.get("customer_id")
        app_user_id = response.get("app_user_id")
        return customer_id, app_user_id


def get_list_customers(lean_app_token: str) -> list[dict]:
    with allure.step(f"Get the list Customers"):
        params = {
            "page_number": 0,
            "page_size": 0
        }
        response = requests.get(url=LEANTECH_URL, headers=get_headers(lean_app_token), params=params).json()["data"]
        return response


def get_customer_by_app_user_id(lean_app_token: str, app_user_id: str) -> dict:
    with allure.step(f"Get the customer by_app_user_id"):
        handler = f"app-user-id/{app_user_id}/"
        response = requests.get(url=f"{LEANTECH_URL}{handler}", headers=get_headers(lean_app_token)).json()
        return response


def get_customer_by_id(lean_app_token: str, customer_id: str) -> dict:
    with allure.step(f"Get the customer customer_id"):
        handler = f"{customer_id}/"
        response = requests.get(url=f"{LEANTECH_URL}{handler}", headers=get_headers(lean_app_token)).json()
        return response

