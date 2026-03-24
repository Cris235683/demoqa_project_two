from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    CARD_LINK= (By.XPATH, ".//div[@class='category-cards']/a")
    locator = (By.XPATH, ".//div[text()='ABC']")

    def get_number_cards(self):
        self.wait_presence_of_element_located(MainPage.CARD_LINK)
        cards = self.driver.find_elements(*MainPage.CARD_LINK)
        return len(cards)
