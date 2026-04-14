import time

import allure
from playwright.sync_api import Playwright, expect


@allure.step("test_standalone")
def test_standalone(playwright: Playwright):

    url = "https://parabank.parasoft.com/parabank/register.htm"
    username = "john"
    password = "demo"


    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)

    page.locator("[name=username]").fill(username)
    page.locator("[name=password]").fill(password)
    page.get_by_text("Log In").click()

    # expect(page.locator(".smallText")).to_have_text("Welcome john Smith")

    #Open an Account
    page.get_by_role("link", name="Open New Account").click()
    page.locator("select#type").select_option(label="SAVINGS")
    # page.locator("#fromAccountId").select_option(index=0)
    page.locator("input[value='Open New Account']").click()

    # expect(page.locator('//div[@id="openAccountForm"]/h1')).to_have_text("Account Opened!")
    account_number = page.locator("#newAccountId").text_content()
    page.locator("#newAccountId").click()

    expect(page.locator("#accountDetails h1")).to_have_text("Account Details")
    expect(page.locator("#accountId")).to_have_text(account_number)


    time.sleep(3)


