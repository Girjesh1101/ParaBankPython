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

