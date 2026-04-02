import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    FULL_NAME_FIELD = (By.XPATH, ".//input[@id='userName']")
    EMAIL_FIELD = (By.XPATH, ".//input[@id='userEmail']")
    ADDRESS_FIELD = (By.XPATH, ".//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS_FIELD = (By.XPATH, ".//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = (By.XPATH, ".//button[@id='submit']")


    @allure.step("Заполнение формы имени")
    def fulling_full_name_field(self, full_name):
        self.fill_up_text_field(TextBoxPage.FULL_NAME_FIELD, full_name)

    @allure.step("Заполнение Email адреса")
    def filling_email_address_field(self, email):
        self.fill_up_text_field(TextBoxPage.EMAIL_FIELD, email)

    @allure.step("Заполнение формы адреса")
    def filling_address_field(self, address):
        self.fill_up_text_field(TextBoxPage.ADDRESS_FIELD, address)

    @allure.step("Заполнение формы permanent адреса")
    def filling_permanent_address_field(self, permanent_address):
        self.fill_up_text_field(TextBoxPage.PERMANENT_ADDRESS_FIELD, permanent_address)

    def scroll_into_button(self):
        self.scroll_to_element(self.SUBMIT_BUTTON)

    @allure.step("Нажимаем кнопку submit")
    def click_submit(self):
        self.click(TextBoxPage.SUBMIT_BUTTON)
    
    @allure.step("Заполнение форм c данными {data_form}")
    def fill_up_text_box_form(self, data_form):
        self.fulling_full_name_field(data_form.get("full_name"))
        self.filling_email_address_field(data_form.get("email"))
        self.filling_address_field(data_form.get("address"))
        self.filling_permanent_address_field(data_form.get("permanent_address"))