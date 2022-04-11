from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys




class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)
    
    def enter_button_pressed(self, element):
        element.send_keys(Keys.ENTER)

    def is_element_visible(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((how, what)))
        except (TimeoutException):
            return False
        return True
    
    def is_element_presented(self, how, what):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((how, what)))
        except (TimeoutException):
            return False
        return True

    def open_in_second_window(self, how, what):
        original_window = self.browser.current_window_handle
        element = self.browser.find_element(how, what)
        element.click()
        WebDriverWait(self.browser, 10).until(EC.number_of_windows_to_be(2))

        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break
