from pyexpat.errors import messages

import allure

from apitest.services.user_services import UserService
from utils.response_validator import ResponseValidator


api_bas_url = "https://practice.expandtesting.com/notes/api"

@allure.title("Create user with valid credentials")
def test_create_user():
    payload = {
        "name":"prem",
        "email":"prem11@yopmail.com",
        "password": "Automation"
    }
    service = UserService(api_bas_url)
    response = service.register_user(payload)
    print(response.url)
    print(response.headers)
    json_response = response.json()
    print(json_response)
    ResponseValidator.validate_status_code(response,201)
    assert "User account created successfully" in json_response["message"]
    assert "id" in json_response["data"]
    assert json_response["data"]["email"] == payload["email"]
    assert  json_response["data"] is not None




