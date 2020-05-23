from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class HomePage:

    URL = "https://www.google.co.uk"

    SEARCH_INPUT = (By.ID, 'the_id_here')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, searchTerm):
        searchInput = self.browser.find_element(*self.SEARCH_INPUT)
        searchInput.send_keys(searchTerm + Keys.RETURN)