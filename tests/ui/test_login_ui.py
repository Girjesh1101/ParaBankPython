import time

import allure

from services.ui.account_services import AccountService
from services.ui.login_service import LoginService
from test_data.factory.user_factory import UserFactory


@allure.title("login with valid credentials")
def test_valid_login(setup):
    page = setup
    user = UserFactory.get_user("valid")

    login_service = LoginService(page)
    login_service.login(user)
    time.sleep(3)
    account_service = AccountService(page)
    account_service.create_new_account()
    account_service.verify_account()

    time.sleep(3)



# @allure.title("login with invalid credentials")
# def test_invalid_login(setup):
#     page = setup
#     user = UserFactory.get_user("invalid")
#     login_service = LoginService(page)
#     login_service.login(user)
#     error_message = login_service.get_error_message()
#     assert error_message == "The username and password could not be verified."

