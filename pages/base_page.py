import allure


from selenium.webdriver.support.expected_conditions import (
    element_to_be_clickable,
    presence_of_element_located,
    visibility_of_element_located
    )
from selenium.webdriver.support.wait import WebDriverWait

from abc import ABC


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Проверка названия сайта')
    def get_title(self):
        return self.driver.title

    @allure.step('Ожидание элемента на странице {locator}')
    def wait_presence_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(
            presence_of_element_located(locator))

    @allure.step('Ожидание видимости элемента на странице {locator}')
    def wait_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(
            visibility_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_clickable_button(self, locator):
        return WebDriverWait(self.driver, 10).until(
            element_to_be_clickable(locator))

    @allure.step('Клик по заданному элементу')
    def click(self, locator):
        self.wait_clickable_button(locator)
        self.wait_visibility_of_element_located(locator)
        self.driver.find_element(*locator).click()

    def fill_up_text_field(self, locator, text):
        self.wait_presence_of_element_located(locator)
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_element(self, locator):
        self.wait_presence_of_element_located(locator)
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            'arguments[0].scrollIntoView(true)', element
            )
