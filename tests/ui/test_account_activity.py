import time

import allure
import pytest

from conftest import BASE_URL, setup
from services.ui.account_overview_service import AccountOverviewService
from services.ui.login_service import LoginService
from test_data.factory.user_factory import UserFactory

@allure.title("capture All the transactions")
def test_capture_all_transactions(setup):

    account_number = "13344"
    page =setup
    user=  UserFactory.get_user("valid")
    service = LoginService(page)
    service.login(user)
    time.sleep(3)

    account_overview_service = AccountOverviewService(page)
    account_overview_service.click_overview(account_number)
    transactions = account_overview_service.capture_transactions_to_allure(month="All", transaction_type="All")
    assert  len(transactions) > 0, "Should have at least one transaction"

    time.sleep(3)

@allure.title("capture only credit transactions")
def test_capture_credit_transactions(setup):
    account_number = "13344"
    page = setup
    user = UserFactory.get_user("valid")
    service = LoginService(page)
    service.login(user)
    time.sleep(3)

    account_overview_service = AccountOverviewService(page)
    account_overview_service.click_overview(account_number)
    transactions = account_overview_service.capture_transactions_to_allure(month="All", transaction_type="Credit")

    for t in transactions:
        assert t["credit"] != "", f"Expect credit transaction but got{t}"

    time.sleep(3)

@allure.title("capture only Debit transactions")
def test_capture_debit_transactions(setup):
    account_number = "13344"
    page = setup
    user = UserFactory.get_user("valid")
    service = LoginService(page)
    service.login(user)
    time.sleep(3)

    account_overview_service = AccountOverviewService(page)
    account_overview_service.click_overview(account_number)
    transactions = account_overview_service.capture_transactions_to_allure(month="All", transaction_type="Debit")
    for t in transactions:
        assert t["debit"] != "", f"Expect credit transaction but got{t}"

    time.sleep(3)

@pytest.mark.parametrize( "month , transaction_type",[
    ("All","All"),
    ("All","Credit"),
    ("All","Debit"),
])
def test_capture_transactions_parameterized(setup, month, transaction_type):
    account_number = "13344"
    page = setup
    user = UserFactory.get_user("valid")
    service = LoginService(page)
    service.login(user)
    time.sleep(3)

    account_overview_service = AccountOverviewService(page)
    account_overview_service.click_overview(account_number)
    transactions = account_overview_service.capture_transactions_to_allure(month=month, transaction_type=transaction_type)
    with allure.step(f"verify transaction for {month} - {transaction_type}") :
        assert transactions is not None, f"Expect transaction but got{transactions}"

