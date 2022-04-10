from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): 
    def should_be_search_box(self):
        assert self.is_element_visible(*MainPageLocators.SEARCH_BOX), "Отсутствует поле поиска"
    
    def search_box_input(self, input_text):
        search_box = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        search_box.click()
        search_box.send_keys(input_text)
    
    def sould_be_suggestions(self):
        assert self.is_element_visible(*MainPageLocators.SUGGESTIONS), "Таблица с подсказками не появилась"