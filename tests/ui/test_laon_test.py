import time

import allure

from services.ui.loan_request_service import LaonRequestService
from services.ui.login_service import LoginService
from test_data.factory.user_factory import UserFactory

@allure.title("Laon Request Tests")
class TestLoanRequest:
    # Step1 : take laon -> capture account_id
    # step 2 : account overview -> select capture account_no -> verify account type should be loan and amount
    # step 3 -> transfer fun from loan account no.
    # step 4 -> verify amount reduce from account and verify remained balance

    LOAN_AMOUNT = "1000"
    DOWN_PAYMENT= "100"
    PAYMENT_AMOUNT = "200"

    @allure.title("Loan Request Denied Tests")
    def test_apply_loan_denied(self, setup):
        page = setup
        user = UserFactory.get_user("valid")
        login_service = LoginService(page)
        login_service.login(user)
        time.sleep(2)
        loan_service = LaonRequestService(page)
        status = loan_service.apply_loan(self.LOAN_AMOUNT, self.DOWN_PAYMENT)

        #assert  loan approved
        assert  status == "Approved",\
            f"Expected Approved but got: {status}"

        # Step 3 - Capture loan account id
        loan_account_id = loan_service.capture_account_no()
        print(f"Loan Account ID: {loan_account_id}")

        allure.attach(
            f"Loan Account ID: {loan_account_id}",
            name="Loan Account ID",
            attachment_type=allure.attachment_type.TEXT,
        )

        time.sleep(2)
        # step 4
        loan_service.verify_loan_account_balance(
            loan_account_no=loan_account_id ,expected_balance=self.LOAN_AMOUNT)

        time.sleep(2)
        #step 5
        page.goto("https://parabank.parasoft.com/parabank/overview.htm")
        page.wait_for_load_state("networkidle")
        from_account = page.locator("table a:first-of-type").first.inner_text()

        time.sleep(2)
        #step 6
        loan_service.pay_back_loan(
            loan_account_no=loan_account_id,
            from_account_id=from_account,
            payment_amount=self.PAYMENT_AMOUNT,
        )

        time.sleep(2)
        # step 7
        # remaining = loan_amount - payment
        remaining_balance = loan_service.verify_remaining_balance(
            loan_account_no=loan_account_id,
            loan_amount=self.LOAN_AMOUNT,
            payment_amount=self.PAYMENT_AMOUNT,
        )
        print(f"Remaining Balance: {remaining_balance}")

        # step 8
        loan_service.verify_transaction_in_history(loan_account_no=loan_account_id,
                                                   payment_amount=self.PAYMENT_AMOUNT)


    @allure.title("Loan Request Denied Tests")
    def test_apply_loan_denied_flow(self, setup):
        LOAN_AMOUNT = "99999999"
        DOWN_PAYMENT = "999"


        page = setup
        user = UserFactory.get_user("valid")
        login_service = LoginService(page)
        login_service.login(user)
        time.sleep(2)
        loan_service = LaonRequestService(page)
        loan_status = loan_service.apply_loan(LOAN_AMOUNT, DOWN_PAYMENT)
        assert loan_status == "Denied"











