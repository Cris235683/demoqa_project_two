class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

class MainPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)