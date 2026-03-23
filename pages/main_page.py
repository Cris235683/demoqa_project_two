from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CARD_LINK=(By.XPATH, ".//div[@class='category-cards']/a")

    def get_number_cards(self):
        cards = self.driver.find_elements(*MainPage.CARD_LINK)
        return len(cards)
