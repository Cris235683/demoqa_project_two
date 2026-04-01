import allure

<<<<<<< HEAD
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
    
=======
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ElementPage(BasePage):
    ELEMENT_QUALITY = (By.XPATH, "(//ul[@class='menu-list'])[1]/li")
    ELEMENT_NAME = lambda name: (By.XPATH, f".//span[text()='{name}']")
    ELEMENT_LINK = (By.XPATH, "//a[@href='https://demoqa.com']")

    @allure.step('Проверка кол-ва элементов в карточке Elements')
    def get_number_elements(self):
        self.wait_presence_of_element_located(ElementPage.ELEMENT_QUALITY)
        cards = self.driver.find_elements(*ElementPage.ELEMENT_QUALITY)
        return len(cards)
    
    @allure.step('Проверка содержимого сайта')
    def check_correct_page_element(self):
        self.wait_presents_of_element_located(ElementPage.ELEMENT_LINK)      
    
    @allure.step('Проверка названия елементов в карточке Elements')
    def is_elements_with_name_correct(self, name):
        self.wait_presence_of_element_located(ElementPage.ELEMENT_NAME(name))
        return self.driver.find_element(*ElementPage.ELEMENT_NAME(name)).is_displayed()
>>>>>>> 6425c18dd60b204ccfe6860779be8ffea7759512
