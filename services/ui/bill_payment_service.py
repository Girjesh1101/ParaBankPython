import allure

from pages.bill_pay_page import BillPaymentPage

class BillPaymentService:
    def __init__(self, page):
        self.page = page
        self.bill_payment = BillPaymentPage(page)


    @allure.step("fill bill payee details")
    def enter_payee_information(self , payee_data):
        self.bill_payment.click_bill_payee_menu_btn()
        self.bill_payment.enter_bill_payee_name(payee_data["name"])
        self.bill_payment.enter_bill_payee_address(payee_data["address"]["street"])
        self.bill_payment.enter_bill_payee_city(payee_data["address"]["city"])
        self.bill_payment.enter_bill_payee_state(payee_data["address"]["state"])
        self.bill_payment.enter_bill_payee_zip_code(payee_data["address"]["zip_code"])
        self.bill_payment.enter_bill_payee_phone(payee_data["phone"])
        self.bill_payment.enter_bill_payee_account_number(payee_data["account_number"])
        self.bill_payment.enter_verify_account_number(payee_data["verify_account_number"])
        self.bill_payment.enter_amount(payee_data["amount"])
        self.bill_payment.select_account()
        self.bill_payment.click_send_payment_btn()

    @allure.step("verify bill paid and capture account number and amount")
    def verify_bill_paid(self):
        account = self.bill_payment.capture_account_number()
        return account