import allure

from conftest import API_BASE_URL
from services.api.account_services import AccountService
from utils.response_validator import ResponseValidator

allure.title("Get account details")
def test_account_details():
    account_id = 13344
    service = AccountService(API_BASE_URL)
    response = service.get_account_details(account_id)
    json_response= response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)

@allure.title("Fetch Account details by customer_id")
def test_account_details_by_customer_id():
    account_id = 13433
    service = AccountService(API_BASE_URL)
    response = service.get_customer_account_details(account_id)
    json_response= response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)


@allure.title("Fetch Account transaction details by account_id")
def test_get_account_transactions():
    account_id = 13344
    service = AccountService(API_BASE_URL)
    response = service.get_customer_account_details(account_id)
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)

@allure.title("Fetch transaction Amount details by account_id")
def test_get_account_transactions():
    account_id = 13344
    service = AccountService(API_BASE_URL)
    response = service.get_account_transaction_by_amount(account_id, 50)
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)


@allure.title("Fetch transaction By Month and Transaction type ")
def test_get_transaction_by_month_and_transaction_type():
    account_id = 13344
    service = AccountService(API_BASE_URL)
    response = service.get_transaction_by_month_trans_type(account_id) # months and type are given by default values
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)

@allure.title("Fetch transaction by date range")
def test_get_transaction_date_range():
    account_id = 13344
    service = AccountService(API_BASE_URL)
    response = service.get_transaction_by_date_range_from_account(account_id)  # dates are given by default values
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)

@allure.title("Fetch transaction by given specific  date ")
def test_get_transaction_specific_date():
    account_id = 13344
    service = AccountService(API_BASE_URL)
    response = service.get_transaction_by_specific_date(account_id)  # date is given by default values
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)

