import allure
from playwright.sync_api import Page

from pages.account_page import AccountPage


class AccountService:
    def __init__(self, page:Page):
        self.page = page
        self.account_page = AccountPage(page)

    @allure.step("Select Account Type")
    def create_new_account(self):

        self.account_page.click_on_open_new_acc_btn()
        self.page.click("text=Open New Account")
        self.page.wait_for_url("**/openaccount.htm")
        self.account_page.get_account_loaded()
        self.account_page.select_account_type()
        self.account_page.select_account_number()
        self.account_page.click_on_new_acc_btn()
        self.account_page.page.wait_for_selector("#openAccountResult", state="visible")

    @allure.step("verify account has created")
    def verify_account(self):
        print(self.page.locator("#openAccountResult h1").text_content())
        congratulation_message = self.account_page.get_congratulation_message()
        print("cong message: ", congratulation_message)
        account_num =  self.account_page.get_account_number()
        print("account number: ", account_num)
        assert "Congratulations" in congratulation_message
        assert account_num is not None
        assert account_num != ""
        return account_num




