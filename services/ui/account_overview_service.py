import allure

from pages.account_overview_page import AccountOverviewPage


class AccountOverviewService:

    def __init__(self, page):
        self.page = page
        self.overview_page = AccountOverviewPage(page)

    @allure.step("Click on Account overview and find account_number")
    def click_overview(self, account_number:str):
        self.overview_page.click_on_account_overview()
        self.overview_page.click_on_account(account_number)
        account_num = self.overview_page.get_account_number()
        print(account_num)
        # assert account_number == account_num


    @allure.step("Get transactions by period and type")
    def get_transactions(self ,month:str = "All", transaction_type: str ="All"):

        self.overview_page.select_activity_periods(month)
        self.overview_page.select_transaction_type(transaction_type)
        self.overview_page.click_go()
        self.overview_page.get_transaction()
        return self.overview_page.get_transaction()

    @allure.step("Capture and attach transaction to Allure")
    def capture_transactions_to_allure(self, month:str = "All", transaction_type: str ="All"):
        transactions = self.get_transactions(month, transaction_type)

        report = f"Period: {month} | Type: {transaction_type}\n"
        report += "-" * 60 + "\n"
        report += f"{'Date':<15}{'Transaction': <25}{'Debit':<10}{'Credit':<10}\n"
        report += "-" * 60 + "\n"

        for t in transactions:
            report += f"{t['date']:<15}{t['transaction']:<25}"
            report += f"{t['debit']:<10}{t['credit']:<10}\n"

        allure.attach(report , name=f"Transactions- {month} - {transaction_type}",
                      attachment_type=allure.attachment_type.TEXT)

        return  transactions

    @allure.step("verify bill paid and capture account number and amount")
    def verify_bill_paid(self):
        amount = self.overview_page.capture_amount()
        account = self.overview_page.capture_account_number()
        completed_message = self.overview_page.verify_bill_paid()
        assert completed_message == "Bill Payment Complete"
        return amount ,account


    @allure.step("verify transaction exists")
    def verify_transaction(self, expected_amount:str):
        transactions = self.get_transactions(month="All", transaction_type="Debit")

        #attached to allure for visibility
        self.capture_transactions_to_allure(month="All", transaction_type="Debit")

        matching = [
            t for t in transactions
            if expected_amount in t['debit']
        ]
        assert  len(matching) > 0, \
        f"no debit transaction found for {expected_amount}"
        return  matching[0]
