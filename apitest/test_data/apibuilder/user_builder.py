class UserBuilder:
    def __init__(self):
        self.name = None
        self.email = None
        self.password = None

    def with_name(self, name):
        self.name = name
        return self

    def with_email(self, email):
        self.email = email
        return self

    def with_password(self, password):
        self.password = password
        return self

    def build(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }