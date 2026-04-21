import allure

from conftest import API_BASE_URL
from services.api.transaction_service import TransactionService
from utils.response_validator import ResponseValidator


@allure.title("Test transaction api")
class TestTransactionApi:

    account_no = 13344
    amount = 50

    @allure.step("Get transaction details")
    def test_transaction_list(self):

        service = TransactionService(API_BASE_URL)
        response = service.get_transaction_list(self.account_no)
        response_json = response.json()
        print(response_json)
        ResponseValidator.validate_status_code(response, 200)

    @allure.step("Get transaction details by amount")
    def test_transaction_by_amount(self):
        service = TransactionService(API_BASE_URL)
        response = service.get_transaction_by_amount(self.account_no , self.amount)
        response_json = response.json()
        print(response_json)
        ResponseValidator.validate_status_code(response, 200)

    @allure.step("Get transaction details by month and transaction type")
    def test_transaction_by_month_type(self):
        service = TransactionService(API_BASE_URL)
        response = service.get_transaction_by_month_type(self.account_no) # given months and trans_type by default
        response_json = response.json()
        print(response_json)
        ResponseValidator.validate_status_code(response, 200)

    @allure.step("Get transaction details by range date")
    def test_transaction_by_range_date(self):
        service = TransactionService(API_BASE_URL)
        response = service.get_transaction_by_range_date(self.account_no)  # given start and end date by default
        response_json = response.json()
        print(response_json)
        ResponseValidator.validate_status_code(response, 200)

    @allure.step("Get transaction details by specific date")
    def test_transaction_by_range_date(self):
        service = TransactionService(API_BASE_URL)
        response = service.get_transaction_by_onDate(self.account_no)  # given today's date by default
        response_json = response.json()
        print(response_json)
        ResponseValidator.validate_status_code(response, 200)




