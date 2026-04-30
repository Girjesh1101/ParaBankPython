from pyexpat.errors import messages

import allure
from faker.proxy import Faker

from apitest.conftest import get_token
from apitest.services.user_services import UserService
from apitest.test_data.factory.user_factory import UserFactory, faker
from utils.response_validator import ResponseValidator

class TestUser:

    faker = Faker()
    api_bas_url = "https://practice.expandtesting.com/notes/api"
    token :str = "ccdb0671584642d68614675c39a4ef88c64900af438d4a559a5d3282dd9c996b"
    # token = get_token()


    @allure.title("Create user with valid credentials")
    def test_create_user(self):

        payload = UserFactory.get_user("valid")
        service = UserService(self.api_bas_url)
        response = service.register_user(payload)
        json_response = response.json()
        ResponseValidator.validate_status_code(response,201)
        assert "User account created successfully" in json_response["message"]
        assert "id" in json_response["data"]
        assert json_response["data"]["email"] == payload["email"]
        assert  json_response["data"] is not None


    @allure.title("Login with valid credentials")
    def test_login_with_valid_credentials(self):
        payload = UserFactory.get_user("login")
        print(payload)
        service = UserService(self.api_bas_url)
        response = service.login_user(payload)
        json_response = response.json()
        print(json_response)
        ResponseValidator.validate_status_code(response,200)
        assert json_response["data"] is not None
        assert "id" in json_response["data"]
        assert json_response["data"]["email"] == payload["email"]
        self.token = json_response["data"]["token"]
        print("token:", self.token)

    @allure.title("GET user Profile")
    def test_get_user_profile(self):
        service = UserService(self.api_bas_url)
        response = service.user_profile(self.token)
        ResponseValidator.validate_status_code(response,200)
        response_json = response.json()
        print(response_json)
        assert "Profile successful"  in response_json["message"]
        assert response_json["data"] is not None

    def test_update_user_profile(self):

        payload = {
            "name":"prem",
            "phone" : "9876543210",
            "company":faker.company()
        }
        service = UserService(self.api_bas_url)
        response = service.fatch_profile(self.token, payload)
        response_json = response.json()
        print(response_json)
        ResponseValidator.validate_status_code(response,200)
        assert "success" in response.json()
        assert response_json["data"]["phone"] == payload["phone"]
        assert response_json["data"]["company"] == payload["company"]


