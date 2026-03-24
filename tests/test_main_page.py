import data

import allure
from pages.main_page import MainPage

@allure.feature("Главная страница")
class TestMainPage:
    @allure.title("Проверка допустимости главной страницы")
    @allure.description("Проверка осуществляется по соответствующему названию заголовка заданного значения")
    def test_main_page_avaliable(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Проверка названия сайта"):
            assert main_page.get_title() == 'demosite'

    @allure.title("Проверка количества карточек на странице = 6")
    @allure.description("На странице должно расположится 6 карточек")
    def test_number_of_cards_is_six(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Проверка количества карточек"):
            assert main_page.get_number_cards() == 6
