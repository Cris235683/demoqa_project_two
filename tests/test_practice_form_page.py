import allure

import data
from pages.practice_form_page import PracticeFormPage


class TestPracticeFormPage:
    @allure.step("Тестирование страницы Practice Form")
    @allure.description("Проверка допустимости страницы Practice Form")
    def test_practice_form_page_is_avaliable(self, driver):
        practice_form_page = PracticeFormPage(driver)
        practice_form_page.open(data.PRACTICE_FORM_URL)

        with allure.step("Проверка правильности формы"):
            assert practice_form_page.is_title_on_page_correct()