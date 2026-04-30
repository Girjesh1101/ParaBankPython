import json

import allure
import requests
from playwright.sync_api import expect

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

    def login_user(self,payload):
        response = requests.post(f"{self.base_url}/users/login", data=payload, headers={"Accept": "application/json"})
        try:
            response_body = response.json()
        except Exception:
            response_body = response.text

        allure.attach(json.dumps(payload, ensure_ascii=False, indent=2),"Request", allure.attachment_type.JSON)
        allure.attach(json.dumps(response_body, ensure_ascii=False, indent=2),"Response", allure.attachment_type.JSON)
        return response


    def user_profile(self, token):
        response = requests.get(f"{self.base_url}/users/profile", headers=
        {"Accept": "application/json",
         "x-auth-token" : token})
        try:
            response_body = response.json()
        except Exception:
            response_body = response.text
        allure.attach(json.dumps(response_body, ensure_ascii=False, indent=2),"Request", allure.attachment_type.JSON)
        return response

    def fatch_profile(self, token , payload):
        response = requests.get(f"{self.base_url}/users/profile", data = payload , headers=
        {"Accept": "application/json",
         "x-auth-token" : token})
        try:
            response_body = response.json()
        except Exception:
            response_body = response.text

        allure.attach(json.dumps(payload, ensure_ascii=False, indent=2),"Request", allure.attachment_type.JSON)
        allure.attach(json.dumps(response_body, ensure_ascii=False, indent=2),"Response", allure.attachment_type.JSON)
        return response
