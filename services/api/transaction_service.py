import json
from datetime import date

import allure
import requests

from utils.json_writer import write_json


class TransactionService:

    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("get transaction list api")
    def get_transaction_list(self, account_no):
        response = requests.get(f"{self.base_url}/accounts/{account_no}/transactions", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "transaction","get_transaction_list")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return  response

    @allure.step("")
    def get_transaction_by_amount(self, account_no, amount):
        response =  requests.get(f"{self.base_url}/accounts/{account_no}/transactions/amount/{amount}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}
        write_json(data, "transaction","get_transaction_by_amount")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("get transaction by month and type")
    def get_transaction_by_month_type(self, account_no, month = "All", transaction_type="All"):
        response = requests.get(f"{self.base_url}/accounts/{account_no}/transactions/month/{month}/type/{transaction_type}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}

        write_json(data, "transaction","get_transaction_by_month_type")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("get transaction by range of date")
    def get_transaction_by_range_date(self, account_no, start_date= str(date.today().strftime("%m-%d-%Y")) , end_date= str(date.today().strftime("%m-%d-%Y"))):
        response = requests.get(f"{self.base_url}/accounts/{account_no}/transactions/fromDate/{start_date}/toDate/{end_date}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}

        write_json(data, "transaction","get_transaction_by_range_date")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step("get transaction details by given specific date")
    def get_transaction_by_onDate(self,account_no , on_date= str(date.today().strftime("%m-%d-%Y"))):
        response = requests.get(f"{self.base_url}/accounts/{account_no}/transactions/onDate/{on_date}", headers={"Accept": "application/json"})
        try:
            data = response.json()
        except ValueError:
            data = {"error": response.text}

        write_json(data, "transaction","get_transaction_by_onDate")
        allure.attach(json.dumps(data, indent=2),"Response", attachment_type=allure.attachment_type.JSON)
        return response






