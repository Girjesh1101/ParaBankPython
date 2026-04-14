import allure

from conftest import API_BASE_URL
from services.api.account_services import AccountService
from utils.response_validator import ResponseValidator

allure.title("Get account details")
def test_account_details():
    account_id = 15675
    service = AccountService(API_BASE_URL)
    response = service.get_accounts(account_id)
    json_response= response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_field_not_none(json_response.get("id"), "id")

