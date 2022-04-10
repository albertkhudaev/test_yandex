from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)

    def is_element_visible(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((how, what)))
        except (TimeoutException):
            return False
        return True