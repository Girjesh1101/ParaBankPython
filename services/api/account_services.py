import json

import allure
import requests

from utils.json_writer import write_json


class AccountService:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Get account details")
    def get_accounts(self, customer_id):
        response = requests.get(f"{self.base_url}/accounts/{customer_id}",
                     headers={"Accept": "application/json"})
        write_json(response.json(),"Accounts","get_account_details_response")
        allure.attach(json.dumps(response.json(), indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step()
    def get_customer_account_details(self, customer_id):
        response = requests.get(f"{self.base_url}/customers/{customer_id}/accounts", headers={"Accept": "application/json"})
        write_json(response.json(), "CustomerAccounts","get_customer_account_details_response")
        allure.attach(json.dumps(response.json(), indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Get account transactions details")
    def get_account_transactions(self, account_id):
        response = requests.get(f"{self.base_url}/accounts/{account_id}/transactions", headers={"Accept": "application/json"})
        write_json(response.json(), "AccountTransactions","get_account_transactions_response")
        allure.attach(json.dumps(response.json(), indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response




