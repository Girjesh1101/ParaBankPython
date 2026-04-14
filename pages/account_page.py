from playwright.sync_api import Page


class AccountPage:
    def __init__(self, page: Page):
        self.page = page
        self.open_new_acc_btn = page.get_by_role("link", name="Open New Account")
        self.account_page_loaded = page.locator("//div[@id='openAccountForm']/h1")
        self.congratulation_message = page.locator('(//div[@id="openAccountResult"]/p)[1]')
        self.get_Account_number = page.locator("#fromAccountId")
        self.get_account_type = page.locator("select#type")
        self.account_number = page.locator("#newAccountId a")
        self.open_acc_btn = page.locator("//input[@value='Open New Account']")

    def click_on_open_new_acc_btn(self):
        self.open_new_acc_btn.click()

    def get_account_loaded(self):
        return self.account_page_loaded.inner_text()

    def select_account_type(self, ):
        self.get_account_type.select_option(label = "SAVINGS")

    def select_account_number(self):
        self.get_Account_number.select_option(index=2)

    def click_on_new_acc_btn(self):
        self.open_acc_btn.click()

    def get_congratulation_message(self):
        return self.congratulation_message.inner_text()

    def get_account_number(self):
        self.page.wait_for_selector("#newAccountId:not([href=''])",
                                    state="visible",
                                    timeout=15000)
        # return self.account_number.inner_text()
        return self.page.locator("#newAccountId").inner_text()

