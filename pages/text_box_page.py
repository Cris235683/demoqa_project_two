import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TextBoxPage(BasePage):
    FULL_NAME_FILED = (By.XPATH, ".//input[@id='userName']")
    USER_EMAIL_FILED = (By.XPATH, ".//input[@id='userEmail']")
    CURRENT_ADDRESS_FILED = (By.XPATH, ".//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS_FILED = (By.XPATH, ".//textarea[@id='permanentAddress']")
    BUTTON_SUBMIT = (By.XPATH, ".//button[@id='submit']")
    CORRECT_FULL_NAME = (By.XPATH, ".//p[@id='name']")
    CORRECT_EMAIL = (By.XPATH, ".//p[@id='email']")
    CORRECT_CURRENT_ADDRESS = (By.XPATH, ".//p[@id='currentAddress']")
    CORRECT_PERMANENT_ADDRESS = (By.XPATH, ".//p[@id='permanentAddress']")

    @allure.step("Заполнение формы имени {full_name}")
    def fill_up_full_name_field(self, full_name):
        self.fill_up_text_field(TextBoxPage.FULL_NAME_FILED, full_name)

    @allure.step("Заполнение формы эмейла {email}")
    def fill_up_user_email_field(self, email):
        self.fill_up_text_field(TextBoxPage.USER_EMAIL_FILED, email)

    @allure.step("Заполнение формы адреса {address}")
    def fill_up_current_address_field(self, address):
        self.fill_up_text_field(TextBoxPage.CURRENT_ADDRESS_FILED, address)

    @allure.step("Заполнение формы перманентного адреса {permanent}")
    def fill_up_permanent_address_field(self, permanent):
        self.fill_up_text_field(
            TextBoxPage.PERMANENT_ADDRESS_FILED, permanent
        )

    # @allure.step()
    def scroll_into_button(self):
        self.scroll_to_element(TextBoxPage.BUTTON_SUBMIT)

    @allure.step("Нажатие на кнопку")
    def click_submit(self):
        self.click(TextBoxPage.BUTTON_SUBMIT)

    @allure.step("Заполнение формы с данными {data_form}")
    def fill_up_text_box_form(self, data_form):
        self.fill_up_full_name_field(data_form.get('full_name'))
        self.fill_up_user_email_field(data_form.get('email'))
        self.fill_up_current_address_field(data_form.get('address'))
        self.fill_up_permanent_address_field(
            data_form.get('permanent_address')
            )

    @allure.step("Получение полного имени")
    def get_full_name(self):
        return self.get_data_only(self.get_text_from_element(
            TextBoxPage.CORRECT_FULL_NAME)
        )

    def get_email(self):
        return self.get_data_only(self.get_text_from_element(
            TextBoxPage.CORRECT_EMAIL)
        )

    def get_current_address(self):
        return self.get_data_only(self.get_text_from_element(
            TextBoxPage.CORRECT_CURRENT_ADDRESS)
        )

    def get_permanenr_addres(self):
        return self.get_data_only(self.get_text_from_element(
            TextBoxPage.CORRECT_PERMANENT_ADDRESS)
        )

    @allure.step(
            "Проверка правильности заполнения формы с данными {data_form}"
        )
    def has_expected_data_on_page(self, data_form):
        return (self.get_full_name() == data_form.get('full_name') and
                self.get_email() == data_form.get('email') and
                self.get_current_address() == data_form.get('address') and
                self.get_permanenr_addres() == data_form.get(
                    'permanent_address'))

    @staticmethod
    def get_data_only(text):
        return text.split(':')[1].strip()
