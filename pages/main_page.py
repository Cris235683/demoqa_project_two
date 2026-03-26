import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CARD_LINK = (By.XPATH, ".//div[@class='category-cards']/a")
    LOGO_LINK = (By.XPATH, ".//header/a")
    FIRST_CARD_NAME = (By.XPATH, ".//h5[text()='Elements']")
    SECOND_CARD_NAME = (By.XPATH, ".//h5[text()='Forms']")

    def get_number_cards(self):
        self.wait_presence_of_element_located(MainPage.CARD_LINK)
        cards = self.driver.find_elements(*MainPage.CARD_LINK)
        return len(cards)
    
    @allure.step("Кликаем по лого")
    def click_on_logo(self):
        self.click(MainPage.LOGO_LINK)

    @allure.step("Проверка имени первой карточки")
    def is_card_with_name(self):
        self.wait_presence_of_element_located(MainPage.FIRST_CARD_NAME)
        return self.driver.find_element(*MainPage.FIRST_CARD_NAME).is_displayed()
    
    @allure.step("Проверка имени второй карточки")
    def second_card_with_name(self):
        self.wait_presence_of_element_located(MainPage.SECOND_CARD_NAME)
        return self.driver.find_element(*MainPage.SECOND_CARD_NAME).is_displayed()
    