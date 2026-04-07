import allure

import data
from pages.alerts_windows_page import AlertsWindowsPage


class TestAlertsWindowsPage:
    @allure.step("Тестирование страницы Alerts")
    @allure.description("Проверка допустимости страницы Alerts")
    def test_alerts_windows_page_is_avaliable(self, driver):
        alerts_windows_page = AlertsWindowsPage(driver)
        alerts_windows_page.open(data.ALERTS_WINDOWS_URL)

        with allure.step("Проверка правильности формы"):
            assert alerts_windows_page.is_title_on_page_correct()
