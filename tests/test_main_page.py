from pages.main_page import MainPage
import data


class TestMainPage:
    def test_main_page_avaliable(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        assert main_page.get_title() == 'demosite'

    def test_number_of_cards_is_six(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        assert main_page.get_number_cards() == 6
