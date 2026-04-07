import allure
import data

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    H1 = (By.XPATH, ".//h1")

    @allure.step("Нашли заголовок Browser Windows Page")
    def get_title_browser_h1(self):
        return self.get_text_from_element(BrowserWindowPage.H1)

    def is_title_on_page_correct(self):
        return self.get_title_browser_h1() == data.BrowserWindowPageData.H1
