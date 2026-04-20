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
    @allure.title("Loan Request Tests")
    def test_apply_loan_e2e(self, setup):
        page = setup
        user = UserFactory.get_user("valid")
        login_service = LoginService(page)
        login_service.login(user)
        time.sleep(2)

        # loan_data = {
        #     "loan_amount": "5000",
        #     "down_payment": "50"
        # }

        loan_service = LaonRequestService(page)
        loan_service.apply_loan()
        loan_status , account_no =  loan_service.verify_loan()
        print(f"loan status  : {loan_status},account number : {account_no}")
        time.sleep(2)











