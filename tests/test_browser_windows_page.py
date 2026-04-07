import allure

import data
from pages.browser_windows_page import BrowserWindowPage


class TestBrowserWindowPage:
    @allure.step("Тестирование страницы Browser")
    @allure.description("Проверка допустимости страницы Browser")
    def test_browser_windows_page_is_avaliable(self, driver):
        browser_windows_page = BrowserWindowPage(driver)
        browser_windows_page.open(data.BROWSER_WINDOWS_URL)

        with allure.step("Проверка правильности формы"):
            assert browser_windows_page.is_title_on_page_correct()