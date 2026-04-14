import allure
from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[name=username]")
        self.password_input= page.locator("[name=password]")
        self.login_btn = page.get_by_text("Log In")
        self.error_message = page.locator(".error")
        self.register_btn = page.get_by_role("button",name="Register")


    @allure.step("Enter username")
    def enter_username(self, username):
        self.username_input.fill(username)

    allure.step("Enter password")
    def enter_password(self, password):
        self.password_input.fill(password)

    @allure.step("click on log In")
    def click_login(self):
        self.login_btn.click()

    @allure.step("Login with credentials")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    allure.step("Get error message")
    def get_error_message(self):
        return self.error_message.inner_text()

    @allure.step("click on register")
    def click_register(self):
        self.register_btn.click()