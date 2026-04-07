import allure
import data

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AlertsWindowsPage(BasePage):
    H1 = (By.XPATH, ".//h1")

    @allure.step("Нашли заголовок Alerts Windows Page")
    def get_title_alerts_h1(self):
        return self.get_text_from_element(AlertsWindowsPage.H1)

    def is_title_on_page_correct(self):
        return self.get_title_alerts_h1() == data.AlertsWindowsPageData.H1
