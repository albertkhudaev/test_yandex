from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): 
    def should_be_search_box(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_BOX), "Отсутствует поле поиска"