import pytest

from apitest.services.user_services import UserService
from apitest.test_data.factory.user_factory import UserFactory

api_bas_url = "https://practice.expandtesting.com/notes/api"
@pytest.fixture(scope="session", autouse=True)
def get_token():
    payload = UserFactory.get_user("login")
    response = UserService(api_bas_url).login_user(payload)
    return response.json()["data"]["token"]

