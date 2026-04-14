from faker import Faker

from test_data.builder.user_builder import UserBuilder

faker = Faker()

class UserFactory:

    @staticmethod
    def get_user(user_type: str):
        if user_type == "valid":
            return (UserBuilder()
                    .with_username("john")
                    .with_password("demo")
                    .build())

        elif user_type == "random":
            return (UserBuilder()
                    .with_username(faker.user_name())
                    .with_password("Automation@2026")
                    .with_first_name(faker.first_name())
                    .with_last_name(faker.last_name())
                    .with_address(faker.address())
                    .with_city(faker.city())
                    .with_state(faker.state())
                    .with_phone(faker.phone_number())
                    .with_ssn(faker.ssn())
                    .build())

        elif user_type == "invalid":
            return (UserBuilder()
                    .with_username("wronguser")
                    .with_password("wrongpass")
                    .build())
        else:
            raise(ValueError("invalid user type"))

