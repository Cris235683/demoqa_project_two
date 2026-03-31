import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementPage(BasePage):
    ELEMENT_QUALITY = (By.XPATH, "(//ul[@class='menu-list'])[1]/li")
    ELEMENT_NAME = lambda name: (By.XPATH, f".//span[text()='{name}']")
    ELEMENT_LINK = (By.XPATH, "//a[@href='https://demoqa.com']")

    @allure.step('Проверка кол-ва элементов в карточке Elements')
    def get_number_elements(self):
        self.wait_presents_of_element_located(ElementPage.ELEMENT_QUALITY)
        cards = self.driver.find_elements(*ElementPage.ELEMENT_QUALITY)
        return len(cards)
    
    @allure.step('Проверка содержимого сайта')
    def check_correct_page_element(self):
        self.wait_presents_of_element_located(ElementPage.ELEMENT_LINK)      
    
    @allure.step('Проверка названия елементов в карточке Elements')
    def is_elements_with_name_correct(self, name):
        self.wait_until_button_clickable(ElementPage.ELEMENT_NAME(name))
        return self.driver.find_element(*ElementPage.ELEMENT_NAME(name)).is_displayed()