import allure
import data

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PracticeFormPage(BasePage):
    H1 = (By.XPATH, ".//h1")
    FIRST_NAME_FILED = (By.XPATH, ".//input[@id='firstName']")
    LAST_NAME_FILED = (By.XPATH, ".//input[@id='lastName']")
    EMAIL_FILED = (By.XPATH, ".//input[@id='userEmail']")
    CHECK_GENDER = (By.XPATH, ".//input[@id='gender-radio-2']")
    NUMBER = (By.XPATH, ".//input[@id='userNumber']")

    @allure.step("Нашли заголовок Practice Form Page")
    def get_title_from_h1(self):
        return self.get_text_from_element(PracticeFormPage.H1)

    def is_title_on_page_correct(self):
        return self.get_title_from_h1() == data.PracticeFormPageData.H1

    @allure.step("Заполнение формы имени {full_name}")
    def fill_up_full_name_field(self, full_name):
        self.fill_up_text_field(PracticeFormPage.FIRST_NAME_FILED, full_name)

    @allure.step("Заполнение формы имени {last_name}")
    def fill_up_last_name_field(self, last_name):
        self.fill_up_text_field(PracticeFormPage.LAST_NAME_FILED, last_name)

    @allure.step("Заполнение формы эмейла {email}")
    def fill_up_email_field(self, email):
        self.fill_up_text_field(PracticeFormPage.EMAIL_FILED, email)

    @allure.step("")
    def check_gender(self):
        self.click(PracticeFormPage.CHECK_GENDER)

    def fill_up_number_phone(self, number):
        self.fill_up_text_field(PracticeFormPage.NUMBER, number)

    @allure.step("Заполнение формы с данными {practice_form}")
    def fill_up_practice_form(self, practice_form):
        self.fill_up_full_name_field(practice_form.get('full_name'))
        self.fill_up_last_name_field(practice_form.get('last_name'))
        self.fill_up_email_field(practice_form.get('email'))
        self.fill_up_number_phone(practice_form.get('number'))
