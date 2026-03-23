from selenium.webdriver.common.by import By
from pages.base_pases import BasePage


class MainPage(BasePage):
    CARD_LINK=(By.XDATH, "//div[@class='cotegry-cords']/e")

    def get_number_cards(self):
        cards = self.driver.find_elements(*MainPage.CARD_LINK)
        return len(cards)