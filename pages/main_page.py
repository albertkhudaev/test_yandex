from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): 
    def should_be_search_box(self):
        assert self.is_element_visible(*MainPageLocators.SEARCH_BOX), "Отсутствует поле поиска"
    
    def should_be_suggestions(self):
        assert self.is_element_visible(*MainPageLocators.SUGGESTIONS), "Таблица с подсказками не появилась"

    def should_be_search_result(self):
        assert self.is_element_visible(*MainPageLocators.SEARCH_RESULT), "Таблица с результатами поиска не появилась"
    
    def should_result_have_link(self, link, n):
        results = []
        first_result = self.browser.find_element(*MainPageLocators.FIRST_RESULT)
        results.append(first_result.text)
        for i in range(2, n + 1):
            xpath = f"//*[@id=\"search-result\"]/li[{i}]/div/div[2]/div[1]/a/b"
            result = self.browser.find_element(By.XPATH, xpath)
            results.append(result.text)
        assert link in results, f"Ссылка на {link} не в первых {n} результатах"

    def should_be_pictures_link(self):
        assert self.is_element_visible(*MainPageLocators.PICTURES_LINK), "Ссылка на картинки отсутствует на странице"

    def search_box_input(self, input_text):
        search_box = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        search_box.click()
        search_box.send_keys(input_text)
    
    def search_box_enter_pressed(self):
        search_box = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        self.enter_button_pressed(search_box)

    def go_to_pictures(self):
        self.open_in_second_window(*MainPageLocators.PICTURES_LINK)
        
