import json
from xml.etree.ElementTree import indent

import allure
import requests

from utils.json_writer import write_json


class CustomerService:

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("get all account from customer")
    def get_customer_accounts(self, customer_id):

        response = requests.get(f"{self.base_url}/customers/{customer_id}/accounts", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "customers" , "get_customer_accounts_details_response")
        allure.attach(json.dumps( data, indent=2), "Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("get customer details")
    def get_customer_details(self, customer_id):
        response = requests.get(f"{self.base_url}/customers/{customer_id}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "customers" , "get_customer_details_response")
        allure.attach(json.dumps( data, indent=2), "Response",attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("get customer position")
    def get_customer_positions(self, customer_id):
        response = requests.get(f"{self.base_url}/customers/{customer_id}/positions", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "customers","customer_positions_response")
        allure.attach(json.dumps( data, indent=2), "Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("create customer account")
    def create_customer_account(self, customer_id, account_type, from_account_id ):

        payload = {
            "customerId": customer_id,
            "newAccountType": account_type,
            "fromAccountId": from_account_id}
        response =  requests.post(f"{self.base_url}/createAccount", json= payload , headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json( payload, "customers","create_customer_account_payload")
        write_json(data, "customers" , "create_customer_account_response")
        allure.attach(json.dumps( payload, indent=2), "Request", attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(data, indent=2), "Response", attachment_type=allure.attachment_type.JSON)
        return response

    def update_customer(self, customer_id, user_data):
        response = requests.post(f"{self.base_url}/customers/update/{customer_id}", json=user_data, headers={"Accept": "application/json", "Content-Type": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(user_data, "customers", "update_customer_account_payload")
        write_json(data, "customers", "create_customer_account_response")
        allure.attach(json.dumps(user_data, indent=2), "Request", attachment_type=allure.attachment_type.JSON)
        allure.attach(json.dumps(data, indent=2), "Response", attachment_type=allure.attachment_type.JSON)
        return response



