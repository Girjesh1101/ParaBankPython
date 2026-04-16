import allure
from playwright.async_api import Page


class BillPaymentPage:

    def __init__(self, page : Page):
        self.page = page
        self.bill_pay_menu_btn = page.get_by_role("link", name="Bill Pay")
        self.input_payee_name = page.locator("input[name='payee.name']")
        self.input_address = page.locator("input[name='payee.address.street']")
        self.input_city = page.locator("input[name='payee.address.city']")
        self.input_state = page.locator("input[name='payee.address.state']")
        self.input_zip_code = page.locator("input[name='payee.address.zipCode']")
        self.input_phone = page.locator("input[name='payee.phoneNumber']")
        self.input_account_number = page.locator("input[name='payee.accountNumber']")
        self.input_verify_account_number = page.locator("input[name='verifyAccount']")
        self.input_amount = page.locator("input[name='amount']")
        self.dropdown_account = page.locator('select[name="fromAccountId"]')
        self.send_pay_btn = page.locator('input[value="Send Payment"]')
        self.capture_account_number_labl = page.locator('#fromAccountId')
        self.verify_bill_paid = page.get_by_role('heading', name= 'Bill Payment Complete' )
        self.amount_label = page.locator("#amount")

    @allure.step("click on bill pay button")
    def click_bill_payee_menu_btn(self):
        self.page.wait_for_load_state("networkidle")
        self.bill_pay_menu_btn.click()

    @allure.step("enter bill payee name")
    def enter_bill_payee_name(self, name):
        self.input_payee_name.fill(name)

    @allure.step("enter bill payee address")
    def enter_bill_payee_address(self, address):
        self.input_address.fill(address)

    @allure.step("enter bill payee city")
    def enter_bill_payee_city(self, city):
        self.input_city.fill(city)

    @allure.step("enter bill payee state")
    def enter_bill_payee_state(self, state):
        self.input_state.fill(state)

    @allure.step("enter bill payee zip_code")
    def enter_bill_payee_zip_code(self, zip_code):
        self.input_zip_code.fill(zip_code)

    @allure.step("enter bill payee phone number")
    def enter_bill_payee_phone(self, phone):
        self.input_phone.fill(phone)

    @allure.step("enter bill payee account number")
    def enter_bill_payee_account_number(self, account_number ):
        self.input_account_number.fill(account_number)

    @allure.step("enter verify account number for payee ")
    def enter_verify_account_number(self, account_number):
        self.input_verify_account_number.fill(account_number)

    @allure.step("enter amount")
    def enter_amount(self, amount):
        self.input_amount.fill(str(amount))

    @allure.step("select account number from the dropdown")
    def select_account(self):
        self.dropdown_account.select_option(index=0)

    @allure.step("click on send payment button")
    def click_send_payment_btn(self):
        self.page.wait_for_load_state("networkidle")
        self.send_pay_btn.click()

    @allure.step("Capture Account Number")
    def capture_account_number(self):
        self.page.wait_for_selector("#fromAccountId", state="visible")
        return self.capture_account_number_labl.inner_text()

    @allure.step("Capture amount")
    def capture_amount(self):
        return self.amount_label.inner_text()

    @allure.step("verify bill paid")
    def verify_bill_paid(self):
        return self.verify_bill_paid.inner_text()