from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class DuckDuckGoSearchPage:
    # URL
    URL = 'https://duckduckgo.com/'

    # Locators
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    # Initializer
    def __init__(self, driver):
        self.driver = driver

    # Interaction methods

    def load(self):
        self.driver.get(self.URL)

    def search(self, phrase):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
