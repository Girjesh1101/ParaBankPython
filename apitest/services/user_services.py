import json

import allure
import requests


class UserService:

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("create user")
    def register_user(self,payload):

        response = requests.post(f"{self.base_url}/users/register", data=payload, headers={
            "Accept": "application/json"
        })

        try:
            response_body = response.json()
        except Exception:
            response_body = response.text

        allure.attach(json.dumps(payload, ensure_ascii=False, indent=2),"Request", allure.attachment_type.JSON)
        allure.attach(json.dumps(response_body, ensure_ascii=False, indent=2),"Response", allure.attachment_type.JSON)

        return  response