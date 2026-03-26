import allure
import pytest

import data
from pages.main_page import MainPage


@allure.feature("Тестирование главной страницы")
class TestMainPage:

    @allure.title("Проверка доступности главной страницы")
    @allure.description("Проверка осуществляется соответствию названию заголовка заданным значением")
    def test_main_page_is_avaliable(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Проверка правильности заголовка"):
            assert main_page.get_title() == "demosite"
    
    @allure.title("Проверка карточек на странице равно 6")
    @allure.description("На странице должно быть 6 карточек")
    def test_number_of_cards_is_six(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Поверка количества карточек"):
            assert main_page.get_number_cards() == 6  

    @allure.title("При клике на лого открывается стартовая страница")
    @allure.description("При клике должна открываться стартовая страница ")
    def test_click_on_logo_go_to_main_page(self, driver):
        """
        1. открыть страницу с заданным url
        2. находим элемент logo который нужно протестировать
        3.  кликнуть по элементу logo
        4. проверить что title соответствует ожидаемому
        """
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        main_page.click_on_logo()

        with allure.step("title соответствует ожидаемому"):
            assert main_page.get_title() == 'demosite' 

    @allure.title("Проверка правильности названия карточки с именем {name_card}")
    @allure.description("Проверка названия карточки")
    @pytest.mark.parametrize(
        "name_card",
         ['Elements',
          'Forms',
          'Alerts, Frame & Windows',
          'Widgets', 
          'Interactions',
          'Book Store Application'
          ])
    def test_name_cards_are_expected_name(self, driver, name_card):
        """
        1. открыть страницу с заданным url
        2. подождали пока загрузится
        3. находим первую карточку стартовой страницы
        4. проверить что название карточки соответствует ожидаемому
        """
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Название первой карточки соответствует ожидаемой"):
            assert main_page.is_card_with_name(name_card) 
        