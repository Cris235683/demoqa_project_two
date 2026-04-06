import allure

import data

from pages.text_box_page import TextBoxPage


class TestTextBox:

    @allure.title("Заполнили данные")
    @allure.description(
        "Заполнили все данные и проверили, что всё правильно выдало"
    )
    def test_text_box_form_with_all_data(self, driver):
        text_box = TextBoxPage(driver)
        text_box.open(data.TEXT_BOX_URL)
        text_box.fill_up_text_box_form(data.DATA_FORM)
        text_box.scroll_into_button()
        text_box.click_submit()

        assert text_box.has_expected_data_on_page(data.DATA_FORM)
