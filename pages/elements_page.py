import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ElementsPage(BasePage):
    ELEMENTS_LINK = (By.XPATH, "//span[@class='text']")
    ELEMENTS_NAME = lambda name: (By.XPATH, f".//span[text()='{name}']")
    CHECK_ELEMENTS_LINK = (By.XPATH, "//a[@header='https://demoqa.com']")
 
    @allure.step("Проверка количества элементов в карточке Elements")
    def get_number_elements(self):
        self.wait_presence_of_element_located(ElementsPage.ELEMENTS_LINK)
        cards = self.driver.find_elements(*ElementsPage.ELEMENTS_LINK)
        return len(cards)
    
    @allure.step("Проверка содержимого сайта")
    def check_correct_page_element(self):
        self.wait_presence_of_element_located(ElementsPage.CHECK_ELEMENTS_LINK)

    @allure.step("Проверка названия элементов в карточке Elements")
    def is_elements_with_name_correct(self, name):
        self.wait_until_button_clickable(ElementsPage.ELEMENTS_NAME(name))
        return self.driver.find_element(*ElementsPage.ELEMENTS_NAME(name)).is_displayed()
    