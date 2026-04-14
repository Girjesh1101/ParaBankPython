import allure


class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected):
        with allure.step(f"Validate status code is {expected}"):
            assert response.status_code == expected, \
            f"Expected {expected} but got {response.status_code}"

    @staticmethod
    def validate_field_not_none(value, field_name):
        with allure.step(f"Validate field {field_name} is None"):
            assert  value is not None , f"Expected {field_name} but got {value}"

    @staticmethod
    def  validate_field_equals(actual, expected, field_name):
        with allure.step(f"Validate {field_name} equals {expected}"):
            assert actual == expected, f"Expected {expected} but got {actual}"
