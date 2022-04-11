from .pages.main_page import MainPage
from .pages.pictures_page import PicturesPage


def test_yandex_search(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()      
    page.should_be_search_box()
    page.search_box_input("Тензор")
    page.should_be_suggestions()
    page.search_box_enter_pressed()
    page.should_be_search_result()
    page.should_result_have_link("tensor.ru", 5)

def test_yandex_pictures(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_pictures_link()
    page.go_to_pictures()
    pictures_page = PicturesPage(browser, browser.current_url)
    pictures_page.should_be_url_images()
    picture_text = pictures_page.return_first_picture_text()
    pictures_page.go_to_first_picture_text()
    pictures_page.should_be_right_text(picture_text)
    pictures_page.open_first_picture()
    pictures_page.should_be_picture()
    first_picture = pictures_page.get_current_picture_url()
    pictures_page.click_button_next()
    second_picture = pictures_page.get_current_picture_url()
    pictures_page.pictures_must_not_be_the_same(first_picture, second_picture)
    pictures_page.click_button_previous()
    current_picture = pictures_page.get_current_picture_url()
    pictures_page.pictures_must_be_the_same(first_picture, current_picture)
