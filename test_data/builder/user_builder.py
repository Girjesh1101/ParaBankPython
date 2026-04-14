class UserBuilder:
    def __init__(self):
        self._username = None
        self._password = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._phone = None
        self._address = None
        self._city = None
        self._state = None
        self._zip_code = None
        self._ssn = None


    def with_username(self, username):
        self._username = username
        return self

    def with_password(self, password):
        self._password = password
        return self

    def with_first_name(self, first_name):
        self._first_name = first_name
        return self

    def with_last_name(self, last_name):
        self._last_name = last_name
        return self

    def with_email(self, email):
        self._email = email
        return self

    def with_phone(self, phone):
        self._phone = phone
        return self

    def with_address(self, address):
        self._address = address
        return self

    def with_city(self, city):
        self._city = city
        return self

    def with_state(self, state):
        self._state = state
        return self

    def with_zip_code(self, zip_code):
        self._zip_code = zip_code
        return self

    def with_ssn(self, ssn):
        self._ssn = ssn
        return self

    def build(self):
        return {
            "username": self._username,
            "password": self._password,
            "first_name": self._first_name,
            "last_name": self._last_name,
            "email": self._email,
            "phone": self._phone,
            "address": {
                "street": self._address,
                "city": self._city,
                "state": self._state,
                "zip_code": self._zip_code,
            },
            "ssn": self._ssn,
        }