import allure
from playwright.async_api import Page


class LoanRequestPage:

    def __init__(self, page : Page):
        self.page = page
        self.request_loan_menu_btn = page.get_by_role("link", name="Request Loan")
        self.input_loan_amount = page.locator("#amount")
        self.input_down_payment = page.locator("#downPayment")
        self.account_dropdown = page.locator("#fromAccountId")
        self.apply_now_btn = page.locator("[value='Apply Now']")

        # loan details page
        self.verify_loan_status_label = page.locator("#loanStatus")
        self.capture_account_id = page.locator("#newAccountId")

    @allure.step("click on request loan")
    def click_on_request_loan(self):
        self.page.wait_for_load_state("networkidle")
        self.request_loan_menu_btn.click()

    @allure.step("enter loan amount")
    def enter_laon_amount(self, loan_amount):
        self.input_loan_amount.fill(loan_amount)

    @allure.step("enter down payment")
    def enter_down_payment(self, down_payment):
        self.input_down_payment.fill(down_payment)

    @allure.step("select account number")
    def select_account(self):
        self.account_dropdown.select_option(index=0)

    @allure.step("click on apply now")
    def click_apply_now(self):
        self.page.wait_for_load_state("networkidle")
        self.apply_now_btn.click()

    @allure.step("get loan status")
    def get_loan_status(self):
        self.page.wait_for_selector("#loanStatus", state="visible", timeout=15000)
        print("Status : ", self.verify_loan_status_label.inner_text())
        return self.verify_loan_status_label.inner_text()


    @allure.step("get account number")
    def get_account_no(self):
        self.page.wait_for_selector("#newAccountId:not([href=''])", state="visible" , timeout=15000)
        print( "Acc:",self.capture_account_id.inner_text())
        return self.capture_account_id.inner_text()