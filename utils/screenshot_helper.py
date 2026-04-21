import allure
from playwright.async_api import Page


class ScreenshotHelper:

    @staticmethod
    def take_screenshot(page : Page , name: str):
        screenshot = page.screenshot()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)

    @staticmethod
    def take_full_screenshot(page : Page , name: str):
        screenshot = page.screenshot(full_page=True)
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
