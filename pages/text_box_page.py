import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextBox(BasePage):
    FULLNAME_FIELD = (By.XPATH, ".//input[@id='userName']")
    EMAIL_FIELD = (By.XPATH, ".//input[@id='userEmail']")
    ADDRESS_FIELD = (By.XPATH, ".//textarea[@id='currentAddress']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[@id='submit']")

    @allure.step("Заполнение всей формы")
    def fill_up_text_field(self, full_name):
        self.fill_up_text_field(self.FULLNAME_FIELD, full_name)

    @allure.step("Заполняем форму с данными")
    def filling_email_address_field(self, data_form):
        self.fill_up_text_field(data_form.get('full_name'))