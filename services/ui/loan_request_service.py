import allure

from pages.loan_request_Page import LoanRequestPage


class LaonRequestService:

    def __init__(self, page):
        self.page = page
        self.laon_request = LoanRequestPage(self.page)

    def click_on_laon_request(self):
        self.laon_request.click_on_request_loan()

    def apply_loan(self):
        self.click_on_laon_request()
        # self.laon_request.enter_laon_amount(laon_data["loan_amount"])
        # self.laon_request.account_dropdown(laon_data["down_payment"])

        self.laon_request.enter_laon_amount("5000")
        self.laon_request.enter_down_payment("50")
        self.laon_request.select_account()
        self.laon_request.click_apply_now()

    def verify_loan(self):
        laon_status = self.laon_request.get_loan_status()
        account_no = self.laon_request.get_account_no()
        return laon_status, account_no

