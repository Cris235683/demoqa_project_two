from abc import ABC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class BasePage(ABC):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)
    
    def get_title(self):
        return self.driver.title
    
    def wait_presence_of_element_located(self, locator):
        locator = (By.XPATH, ".//div[text()='ABC']")

        return WebDriverWait(self.driver, 10).until(self.wait_presence_of_element_located(locator))

    #def wait_clickable_button(self):
        