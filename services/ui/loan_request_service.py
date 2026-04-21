import allure
from playwright.async_api import Page

from conftest import BASE_URL
from pages.loan_request_Page import LoanRequestPage
from utils.screenshot_helper import ScreenshotHelper


class LaonRequestService:

        def __init__(self, page:Page):
            self.page = page
            self.laon_request = LoanRequestPage(self.page)
            self.screenshot = ScreenshotHelper()

        def click_on_laon_request(self):
            self.laon_request.click_on_request_loan()

        def apply_loan(self, loan_amount: str, down_payment:str):
            self.click_on_laon_request()
            self.laon_request.enter_laon_amount(loan_amount)
            self.laon_request.enter_down_payment(down_payment)
            self.laon_request.select_account()
            self.screenshot.take_full_screenshot(self.page, "Loan form filled")
            self.laon_request.click_apply_now()
            status = self.laon_request.get_loan_status()
            self.screenshot.take_screenshot(self.page, f"Loan Result - {status}")

            allure.attach(
                f"Loan Amount: ${loan_amount}\n"
                f"Down Payment: ${down_payment}\n"
                f"status: ${status}\n",
                name= "Loan Request Details",
                attachment_type=allure.attachment_type.TEXT,
            )
            return status

        @allure.step("Get Loan account details")
        def capture_account_no(self):
            account_no = self.laon_request.get_account_no()
            return account_no

        @allure.step("verify loan account balance")
        def verify_loan_account_balance(self, loan_account_no: str, expected_balance: str):

            self.page.goto(f"{BASE_URL}/activity.htm?id={loan_account_no}")
            self.page.wait_for_load_state("networkidle")

            self.screenshot.take_full_screenshot(self.page, "Loan Account Details")

            #Get balance from account
            balance = self.page.locator("table:first-of-type tr:nth-child(3) td:nth-child(2)").first.inner_text()
            allure.attach(
                f"Loan Account : ${loan_account_no}\n"
                f"Expected Balance: ${expected_balance}\n"
                f"Actual Balance: ${balance}\n",
                name= "Loan Account Balance",
                attachment_type=allure.attachment_type.TEXT,
            )

            assert  expected_balance in balance, \
            f"Expected Balance: ${expected_balance} but got {balance}"
            return balance

        @allure.step("Pay Back loan amount")
        def pay_back_loan(self, loan_account_no: str, from_account_id:str, payment_amount: str):

            # Nevigate to transfer form
            self.page.goto(f"{BASE_URL}/transfer.htm")
            self.page.wait_for_load_state("networkidle")

            self.page.locator("#amount").fill(payment_amount)
            self.page.locator("#fromAccountId").select_option(value=loan_account_no)

            self.page.locator("#toAccountId").select_option(value=from_account_id)
            self.screenshot.take_screenshot(self.page, "Transfer Payment Filled")

            #submit
            self.page.locator("[value='Transfer']").click()
            self.page.wait_for_load_state("networkidle")

            allure.attach(
                f"Payment Account : ${payment_amount}\n"
                f"From Account : ${from_account_id}\n"
                f"To Loan Account : ${loan_account_no}\n",
                name= "Loan Payment Details",
                attachment_type=allure.attachment_type.TEXT,
            )

        @allure.step("Verify remaining balance after payment")
        def verify_remaining_balance(self, loan_account_no: str, loan_amount: str , payment_amount: str):

          #Calculating expected remaining balance dynamically
          remaining =  float(loan_amount) - float(payment_amount)
          expected_remaining = f"{remaining:.2f}"
          allure.attach(
              f"Loan Amount: ${loan_amount}\n"
              f"Payment Made: ${payment_amount}\n"
              f"Expected Remaining: ${expected_remaining}",
              name="Balance Calculation",
              attachment_type=allure.attachment_type.TEXT
          )

          self.page.goto(f"{BASE_URL}/activity.htm?id={loan_account_no}")
          self.page.wait_for_load_state("networkidle")

          self.screenshot.take_screenshot(self.page, "Balance After payment")

          balance_text  = self.page.locator("table:first-of-type tr:nth-child(3) td:nth-child(2)").first.inner_text()

          actual_balance = balance_text.replace("$","").replace(",","")
          print("actual_balance: ", actual_balance)
          assert  actual_balance == expected_remaining, \
            f"Expected ${expected_remaining} but got ${actual_balance}"
          return actual_balance

        @allure.step("Verify payment  appears in transaction")
        def verify_transaction_in_history(self, loan_account_no: str, payment_amount: str):
            self.page.goto(f"{BASE_URL}/activity.htm?id={loan_account_no}")
            self.page.wait_for_load_state("networkidle")

            self.screenshot.take_full_screenshot(self.page, "Transaction History")

            # get all transaction row
            rows = self.page.locator("table#transactionTable tbody tr").all()
            transactions = []

            for row in rows:
                cells=  row.locator("td").all()
                if len(cells) >= 4:
                    transactions.append({
                        "date":cells[0].inner_text(),
                        "transaction":cells[1].inner_text(),
                        "debit":cells[2].inner_text(),
                        "credit":cells[3].inner_text()
                    })

            # FInd matching payment transaction
            payment_str = f"{ float(payment_amount):.2f}"
            matching = [
                t for t in transactions
                if payment_str in t["debit"]
            ]

            # Attach all transactions to allure
            report = f"{'Date':<15}{'Transaction':<30}{'Debit':<12}{'Credit':<12}\n"
            report += "-" * 70 + "\n"
            for t in transactions:
                report += (f"{t['date']:<15}{t['transaction']:<30}"
                           f"{t['debit']:<12}{t['credit']:<12}\n")

            allure.attach(
                report,
                name="Transaction History After Payment",
                attachment_type=allure.attachment_type.TEXT
            )

            assert len(matching) > 0, \
                f"Payment of ${payment_amount} not found in transactions!"

            return transactions



