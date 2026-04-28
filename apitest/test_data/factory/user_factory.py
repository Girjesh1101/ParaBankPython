from faker.proxy import Faker

faker = Faker()
class UserFactory:

    @staticmethod
    def get_user(user_type:str):

        user_data = {
            "valid":{
                "name":faker.name(),
                "email":faker.email(),
                "password":faker.password()
                },
            "invalid":{
                "name":"",
                "email": "",
                "password": ""
                }
        }
        return user_data[user_type]