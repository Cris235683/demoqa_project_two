from abc import ABC

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    element_to_be_clickable,
    )


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие страницы {url}")
    def open(self, url):
        self.driver.get(url)
    
    @allure.step("Проверка заголовка")
    def get_title(self):
        return self.driver.title
    
    @allure.step("Ожидание элемента страницы {locator}")
    def wait_presence_of_element_located(self, locator):
        locator = (By.XPATH, ".//div[text()='ABC']")

        return WebDriverWait(self.driver, 10).until(presence_of_element_located(locator))

    def wait_clickable_button(self, locator):
        return WebDriverWait(self.driver, 10).until(element_to_be_clickable(locator))
        