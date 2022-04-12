from .base_page import BasePage
from .locators import PicturesPageLocators


class PicturesPage(BasePage): 
    def should_be_url_images(self):
        assert "https://yandex.ru/images/" in self.browser.current_url, "Перешли на неверный url"

    def should_be_right_text(self, text):
        query = self.browser.execute_script("return document.getElementsByClassName('input__control')[0].value")
        assert text == query, f"На картинке был текст \'{text}\', а в поиске текст \'{query}\'"

    def should_be_picture(self):
        assert self.is_element_presented(*PicturesPageLocators.PICTURE), "Картинка не открылась"

    def pictures_must_not_be_the_same(self, first_picture, second_picture):
        assert first_picture != second_picture, "Картинка не переключается"

    def pictures_must_be_the_same(self, first_picture, second_picture):
        assert first_picture == second_picture, "При нажатии кнопки назад картинка меняется не на прошлое изображение"
    
    def return_first_picture_text(self):
        return self.browser.find_element(*PicturesPageLocators.FIRST_PICTURE_TEXT).text

    def go_to_first_picture_text(self):
        first_picture = self.browser.find_element(*PicturesPageLocators.FIRST_PICTURE_TEXT)
        first_picture.click()

    def open_first_picture(self):
        self.is_element_visible(*PicturesPageLocators.FIRST_PICTURE)
        first_picture = self.browser.find_element(*PicturesPageLocators.FIRST_PICTURE)
        first_picture.click()

    def get_current_picture_url(self):
        element = self.browser.find_element(*PicturesPageLocators.PICTURE)
        return element.get_attribute("src")

    def click_button_next(self):
        button = self.browser.find_element(*PicturesPageLocators.BUTTON_NEXT)
        button.click()

    def click_button_previous(self):
        button = self.browser.find_element(*PicturesPageLocators.BUTTON_PREVIOUS)
        button.click()
