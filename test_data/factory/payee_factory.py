from faker import Faker

faker = Faker()
class PayeeFactory:

    @staticmethod
    def get_payee(payee_type):
        payee_data =  {
            "valid" : {
                "name" : faker.name(),
                "address":{
                    "street": faker.address(),
                    "city": faker.city(),
                    "state": faker.state(),
                    "zip_code": "400001",
                },
                "phone": "9876543210",
                # "account_number": faker.random_int(min = 100 , max=10000),
                "account_number": "12345",
                "verify_account_number": "12345",
                "amount": faker.random_int(min=5, max=100),
            },
            "invalid" : {
                "name": "",
                "address": {
                    "street": "",
                    "city": "",
                    "state": "",
                    "zip_code": "",
                },
                "phone": "",
                "account_number": "",
                "verify_account_number":"",
                "amount": "",
            }

        }
        return payee_data[payee_type]