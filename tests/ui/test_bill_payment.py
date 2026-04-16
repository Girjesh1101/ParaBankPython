import time

import allure

from services.ui.account_overview_service import AccountOverviewService
from services.ui.bill_payment_service import BillPaymentService
from services.ui.login_service import LoginService
from test_data.factory.payee_factory import PayeeFactory
from test_data.factory.user_factory import UserFactory


@allure.title("Bill Payment Test")
class TestBillPayment:

    @allure.title("Bill Payment Test")
    def test_bill_payment_successfully(self, setup):

        #Login
        page = setup
        user =UserFactory.get_user("valid")
        login_service = LoginService(page)
        login_service.login(user)
        time.sleep(2)
        #bill payment
        payee_data = PayeeFactory.get_payee("valid")
        print("payee data :",payee_data)
        expected_amount = str(payee_data["amount"])

        bill_service = BillPaymentService(page)
        bill_service.enter_payee_information(payee_data)
        account_number = bill_service.verify_bill_paid()
        print("account_number :",account_number)
        time.sleep(3)
        #verify
        account_overview= AccountOverviewService(page)
        account_overview.click_overview(str(account_number))
        transaction = account_overview.capture_transactions_to_allure(month="All",transaction_type="Debit")

        with allure.step(f"Verify {expected_amount} debit appear in transactions"):
            assert any(txn["debit"] == int(expected_amount) for txn in transaction)
            # account_overview.verify_transaction(expected_amount)
            # assert  transaction["debit"] == int(expected_amount)
            # assert transaction["date"] is not None
        time.sleep(3)