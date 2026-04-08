import allure

import time
import data
from pages.practice_form_page import PracticeFormPage


class TestPracticeFormPage:
    @allure.title("Тестирование страницы Practice Form")
    @allure.description("Проверка допустимости страницы Practice Form")
    def test_practice_form_page_is_avaliable(self, driver):
        practice_form_page = PracticeFormPage(driver)
        practice_form_page.open(data.PRACTICE_FORM_URL)

        with allure.step("Проверка правильности формы"):
            assert practice_form_page.is_title_on_page_correct()

    @allure.title("Заполнение формы")
    @allure.description("Заполнение формы всеми данными")
    def test_practice_form_with_all_data(self, driver):
        practice_form = PracticeFormPage(driver)
        practice_form.open(data.PRACTICE_FORM_URL)
        practice_form.fill_up_practice_form(data.PRACTICE_FORM)
        practice_form.check_gender()
        time.sleep(5)
