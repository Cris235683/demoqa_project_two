import allure
import pytest

import data
from pages.main_page import MainPage
from pages.elements_page import ElementPage


@allure.feature("Тестирование главной страницы")
class TestMainPage:

    @allure.title("Проверка доступности главной страницы")
    @allure.description(
        "Проверка осуществляется соответствию названию заголовка заданным значением"
    )
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
            assert main_page.get_number_cards() == len(
                data.CARD
            )

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

    @allure.title(
            "Проверка правильности названия карточки с именем {name_card}"
        )
    @allure.description("Проверка названия карточки")
    @pytest.mark.parametrize("name_card", data.CARD)
    def test_name_card_is_element(self, driver, name_card):

        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        with allure.step("Название карточки соответствует ожидаемой"):
            assert main_page.is_card_with_name(name_card)

    def test_go_to_elements_page(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)
        main_page.go_to_elements_page()
        elements_page = ElementPage(
            main_page.driver
            )

        with allure.step("Проверка названия сайта"):
            assert data.TITLE_OF_ELEMENT_PAGE == elements_page.get_title_from_page()
