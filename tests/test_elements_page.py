import allure
import pytest

import data
from pages.elements_page import ElementPage


class TestElements:
    @allure.title("Проверка открытия сайта")
    @allure.description("Сайт открывается с нужным заголовком")
    def test_element_page_is_available(self, driver):
        elements_page = ElementPage(driver)
        elements_page.open(data.ELEMENTS_URL)
        
        with allure.step("Проверка названия сайта"):
            assert elements_page.get_title() == 'demosite'

    @allure.title("Проверка корректности открытия сайта")
    @allure.description("Сайт открывается с нужным заголовком")
    def test_check_correct_open_element_page(self, driver):
        elements_page = ElementPage(driver)
        elements_page.open(data.ELEMENTS_URL)

        with allure.step("Заголовок корректный"):
            assert elements_page.check_correct_page_element

    @allure.title("Проверка что в каточке 9 елементов")
    @allure.description("В карточке должно быть 9 елементов")
    def test_number_of_cards_in_elements_is_nine(self, driver):
        elements_page = ElementPage(driver)
        elements_page.open(data.ELEMENTS_URL)
        
        with allure.step("Проверка кол-ва карточек"):
            assert elements_page.get_number_elements() == 9

    @allure.title("Проверка правильности названия елемента с именем {name_card}")
    @allure.description("Название елемента с именем {name_card}")
    @pytest.mark.parametrize("name_card", data.ELEMENTS)
    def test_name_elements_in_card_is_correct(self, driver, name_card):
        elements_page = ElementPage(driver)
        elements_page.open(data.ELEMENTS_URL)

        with allure.step("Название елементов соответствует ожиданию"):
            assert elements_page.is_elements_with_name_correct(name_card)
