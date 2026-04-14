import allure
import pytest
from playwright.sync_api import Page

from utils.logger import log_file

BASE_URL = "https://parabank.parasoft.com/parabank"
API_BASE_URL = "https://parabank.parasoft.com/parabank/services/bank"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def api_base_url():
    return API_BASE_URL

# @pytest.fixture(scope="session", autouse=True)
# def auth_token():

@pytest.fixture(scope="function")
def setup(page:Page):
    page.goto(f"{BASE_URL}/index.htm")
    return page

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item ,call):
    outcome =yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("setup") or item.funcargs.get("page")

        if page:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        try:
            with open(log_file, "r") as f:
                allure.attach(
                    f.read(),
                    name="Execution Logs",
                    attachment_type=allure.attachment_type.TEXT
                )
        except FileNotFoundError:
            pass
