class TokenManager:
    _token = None
    _customer_id = None

    @classmethod
    def get_token(cls):
        return cls._token

    @classmethod
    def set_token(cls, token):
        cls._token = token

    @classmethod
    def get_customer(cls):
        return cls._customer_id

    @classmethod
    def set_customer(cls, customer_id):
        cls._customer_id = customer_id

