import allure
import pytest
from assertpy import assert_that

from tests.config.environments import Environments
from tests.req import get_list_customers, get_customer_by_id, get_customer_by_app_user_id, create_customer

LEAN_APP_TOKEN = Environments().get_token


@allure.description("Test the customer creation process")
class TestCustomerCreation:
    def test_list_customers(self, customer):
        customer_id, app_user_id = customer
        with allure.step(f"Check that user with {customer_id=} and {app_user_id=} in the list of customers"):
            list_of_customers = get_list_customers(LEAN_APP_TOKEN)
            assert_that(list_of_customers).contains(customer_id, app_user_id)

    def test_get_customer_by_app_user_id(self, customer):
        customer_id, app_user_id = customer
        with allure.step(f"Check that user exists by app_user_id with {customer_id=} and {app_user_id=} "):
            customer_dict = get_customer_by_app_user_id(LEAN_APP_TOKEN, app_user_id)
            assert_that(customer_dict).contains_value(customer_id, app_user_id)

    def test_get_customer_by_id(self, customer):
        customer_id, app_user_id = customer
        with allure.step(f"Check that user exists by customer_id with {customer_id=} and {app_user_id=} "):
            customer_dict = get_customer_by_id(LEAN_APP_TOKEN, customer_id)
            assert_that(customer_dict).contains_value(customer_id, app_user_id)


@pytest.fixture(scope="module")
def customer():
    customer_id, app_user_id = create_customer(LEAN_APP_TOKEN)
    return customer_id, app_user_id
