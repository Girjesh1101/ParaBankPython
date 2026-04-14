import allure
from playwright.sync_api import Page

from pages.login_page import LoginPage


class LoginService:

    def __init__(self, page:Page):
        self.login_page = LoginPage(page)

    @allure.step("Login with valid credentials")
    def login(self, user):
        self.login_page.login(user["username"], user["password"])

    @allure.step("Get error message")
    def get_error_message(self):
        self.login_page.get_error_message()