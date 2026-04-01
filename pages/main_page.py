import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CARD_LINK = (By.XPATH, ".//div[@class='category-cards']/a")
    CARD_NAME = lambda name: (By.XPATH, f".//h5[text()='{name}']")
    LOGO_LINK = (By.XPATH, ".//header/a")
    ELEMENTS_LINK = (By.XPATH, "//a[@href='/elements']")
    

    def get_number_cards(self):
        self.wait_presence_of_element_located(MainPage.CARD_LINK)
        cards = self.driver.find_elements(*MainPage.CARD_LINK)
        return len(cards)
    
    @allure.step("Кликаем по лого")
    def click_on_logo(self):
        self.click(MainPage.LOGO_LINK)


    @allure.step("Проверка имени карточки")
    def is_card_with_name(self, name):
        self.wait_presence_of_element_located(MainPage.CARD_NAME(name))
        return self.driver.find_element(*MainPage.CARD_NAME(name)).is_displayed()
    
    def go_to_elements_page(self):
        self.click(MainPage.ELEMENTS_LINK)

    