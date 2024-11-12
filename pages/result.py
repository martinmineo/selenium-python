from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, driver):
        self.driver = driver

    def search_input_value(self):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.driver.title
