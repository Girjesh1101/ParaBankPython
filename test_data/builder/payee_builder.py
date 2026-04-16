import allure


class BillPayeeBuilder:

    def __init__(self):
        self.payee_name = None
        self.payee_address = None
        self.payee_city = None
        self.payee_state = None
        self.payee_zip_code = None
        self.payee_phone = None
        self.payee_account_number = None
        self.verify_account_number = None
        self.amount = None
        self.select_account_number = None

    def with_payee_name(self, payee_name):
        self.payee_name = payee_name
        return self

    def with_payee_address(self, payee_address):
        self.payee_address = payee_address
        return self

    def with_payee_city(self, payee_city):
        self.payee_city = payee_city
        return self

    def with_payee_state(self, payee_state):
        self.payee_state = payee_state
        return self

    def with_payee_zip_code(self, payee_zip_code):
        self.payee_zip_code = payee_zip_code
        return self

    def with_payee_phone(self, payee_phone):
        self.payee_phone = payee_phone
        return self

    def with_payee_account_number(self, payee_account_number):
        self.payee_account_number = payee_account_number
        return self

    def with_payee_verify_account_number(self, verify_account_number):
        self.verify_account_number = verify_account_number
        return self

    def with_payee_amount(self, amount):
        self.amount = amount
        return self

    def with_payee_select_account_number(self, select_account_number):
        self.select_account_number = select_account_number
        return self

    def build(self):
        return {
            "name": self.payee_name,
            "address": {
                "street": self.payee_address,
                "city": self.payee_city,
                "state": self.payee_state,
                "zip_code": self.payee_zip_code,
            },
            "phone": self.payee_phone,
            "account_number": self.payee_account_number,
            "verify_account_number": self.verify_account_number,
            "amount": self.amount,
        }