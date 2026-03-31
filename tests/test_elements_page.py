import allure
import pytest

import data
from pages.elements_page import ElementsPage


class TestMainPage:

    @allure.title("Проверка открытия сайта")
    @allure.description("Сайт открывается с нужным заголовком")
    def test_element_page_is_avaliable(self, driver):
        elements_page = ElementsPage(driver)
        elements_page.open(data.ELEMENTS_URL)

        with allure.step("Проверка названия сайта"):
            assert elements_page.get_title() == "demosite"

    @allure.title("Проверка корректости открытия сайта")
    @allure.description("Сайт открывается с нужным заголовком")
    def test_check_correct_open_element_page(self, driver):
        elements_page = ElementsPage(driver)
        elements_page.open(data.ELEMENTS_URL)

        with allure.step("Заголовок корректный"):
            assert elements_page.check_correct_page_element  

    @allure.title("Проверка правильности названия элемента с именем {name_card}")
    @allure.description("Проверка названия элемента")
    @pytest.mark.parametrize(
        "name_card",
         ['Text Box',
          'Check Box',
          'Radio Button',
          'Web Tables', 
          'Buttons',
          'Links',
          'Broken Links - Images',
          'Upload and Download',
          'Dynamic Properties'
          ])
    def test_name_element_in_card_is_correct(self, driver, name_card):
        elements_page = ElementsPage(driver)
        elements_page.open(data.ELEMENTS_URL)

        with allure.step("Название элементов соответствует ожиданию"):
            assert elements_page.is_elements_with_name_correct(name_card) 
            