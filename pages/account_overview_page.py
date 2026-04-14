import allure
from playwright.async_api import Page


class AccountOverviewPage():

    def __init__(self, page : Page):
        self.page = page
        self.acc_overview_btn_manu = page.get_by_role("link", name="Accounts Overview")
        self.account_table = page.locator("tr")
        self.account_no_label = page.locator("#accountId")
        self.available_balance_label = page.locator("#balance")
        self.activity_periods = page.locator("select[name='month']")
        self.transaction_type = page.locator("select#transactionType")
        self.go_btn = page.locator('input[value="Go"]')
        self.transaction_table = page.locator("table#transactionTable tbody tr")
        self.balance = page.locator("table.balance td:nth-child(2)")

    @allure.step("click on account overview")
    def click_on_account_overview(self):
        self.acc_overview_btn_manu.click()

    @allure.step("click account number")
    def click_on_account(self, account_no):
        self.page.wait_for_selector("tr")
        acc_btn = self.account_table.filter( has_text=account_no)
        acc_btn.get_by_role("link", name=account_no).click()


    @allure.step("verify account number")
    def get_account_number(self):
        self.page.wait_for_selector("#accountId", state="visible")
        return self.account_no_label.inner_text()

    @allure.step("Select activity periods")
    def select_activity_periods(self, month:str):
        self.activity_periods.select_option(label=month)

    @allure.step("select transaction type")
    def select_transaction_type(self, transaction_type):
        self.transaction_type.select_option(label=transaction_type)

    @allure.step("click go")
    def click_go(self):
        self.go_btn.click()
        self.page.wait_for_load_state("networkidle")

    @allure.step("Get all transactions")
    def get_transaction(self):
        transactions = []
        rows = self.transaction_table.all()
        for row in rows:
            cells = row.locator("td").all()
            if len(cells) >= 4:
                date = cells[0].inner_text().strip()
                transaction = cells[1].inner_text().strip()
                debit = cells[2].inner_text().strip()
                credit = cells[3].inner_text().strip()
                transactions.append({
                    "date" : date,
                    "transaction" : transaction,
                    "debit" : debit,
                    "credit" : credit
                })
        return transactions

    @allure.step("Get balance amount")
    def get_balance(self):
        return self.page.locator("table.balance").inner_text()





