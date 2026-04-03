import time

import data
from pages.text_box_page import TextBoxPage

class TestTextBox():
    def test_text_box_form_with_all_data(self, driver):
        text_box = TextBoxPage(driver)
        text_box.open(data.Text_Box_URL)
        text_box.fill_up_text_box_form(data.data_form)
        text_box.scroll_into_button()
        text_box.click_submit()
        time.sleep(2)