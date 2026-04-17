import json
from datetime import date

import allure
import requests

from utils.json_writer import write_json


class AccountService:
    def __init__(self, base_url):
        self.base_url = base_url


    @allure.step("get account details")
    def get_account_details(self, account_id):

        response = requests.get(f"{self.base_url}/accounts/{account_id}", headers={"Accept": "application/json"})
        write_json(response.json(), "CustomerAccounts","get_customer_account_details_response")
        allure.attach(json.dumps(response.json(), indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data,"Accounts","get_account_details_response")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Get customer account details")
    def get_customer_account_details(self, customer_id):
        response = requests.get(f"{self.base_url}/customers/{customer_id}/accounts", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "CustomerAccounts","get_customer_account_details_response")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Get account transactions details")
    def get_account_transactions(self, account_id):
        response = requests.get(f"{self.base_url}/accounts/{account_id}/transactions", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "Transactions","get_account_transactions_response")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step("Get transaction by amount")
    def get_account_transaction_by_amount(self, account_id, amount):
        response  = requests.get(f"{self.base_url}/accounts/{account_id}/transactions/amount/{amount}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data , "Transactions", "get_account_transaction_by_amount_response")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Get transaction by month and transaction type")
    def get_transaction_by_month_trans_type(self, account_id, month="All", trans_type="All"):
        response =  requests.get(f"{self.base_url}/accounts/{account_id}/transactions/month/{month}/type/{trans_type}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "Transactions","get_transaction_by_month_trans_type_response")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("Get transaction by date range from account")
    def get_transaction_by_date_range_from_account(self, account_id, from_date= str(date.today().strftime("%m-%d-%Y")), to_date= str(date.today().strftime("%m-%d-%Y"))):
        print("date", from_date)
        response = requests.get(f"{self.base_url}/accounts/{account_id}/transactions/fromDate/{from_date}/toDate/{to_date}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "Transactions","get_transaction_by_date_range_from_account_response")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    def get_transaction_by_specific_date(self, account_id, on_date=str(date.today().strftime("%m-%d-%Y"))):
        print("date", on_date)
        response = requests.get(
            f"{self.base_url}/accounts/{account_id}/transactions/onDate/{on_date}",headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "Transactions", "get_transaction_by_specific_date_response")
        allure.attach(json.dumps(data, indent=2), "Response", attachment_type=allure.attachment_type.JSON)
        return response





