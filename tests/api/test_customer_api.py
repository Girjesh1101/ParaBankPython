import allure

from conftest import API_BASE_URL
from services.api.account_services import AccountService
from services.api.customer_services import CustomerService
from utils.response_validator import ResponseValidator

customer_id =12212
account_no = 61629


@allure.title("Get Customer Accounts details")
def test_get_customer_accounts():

    service = CustomerService(API_BASE_URL)
    response =  service.get_customer_accounts(customer_id)
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)
    # ResponseValidator.validate_field_not_none(json_response.get("id"), "customer_id")

@allure.title("Get Customer details")
def test_get_customer_details():
    service = CustomerService(API_BASE_URL)
    response = service.get_customer_details(customer_id)
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_field_not_none(json_response.get("id"), "customer_id")

@allure.title("Get Customer Position test")
def test_get_customer_position_test():
    service = CustomerService(API_BASE_URL)
    response = service.get_customer_positions(customer_id)
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)
    # ResponseValidator.validate_field_not_none(json_response.get("customerId"), "customerId")


@allure.title(" create customer account with valid data")
def test_create_customer():
    service = CustomerService(API_BASE_URL)
    response = service.create_customer_account(customer_id,1,22335)
    response_json = response.json()
    print(response_json)
    ResponseValidator.validate_status_code(response, 200)
    account_num =  response_json.grt("id")



