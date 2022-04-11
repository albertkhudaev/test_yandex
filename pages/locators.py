from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_BOX = (By.CSS_SELECTOR, "input#text")
    SUGGESTIONS = (By.CSS_SELECTOR, "body > div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile")
    SEARCH_RESULT = (By.CSS_SELECTOR, "#search-result")
    FIRST_RESULT = (By.XPATH, "//*[@id=\"search-result\"]/li[1]/div/div[1]/div[2]/div[1]/a/b")
    PICTURES_LINK = (By.CSS_SELECTOR, "[data-id=\"images\"]")


class PicturesPageLocators():
    FIRST_PICTURE_TEXT = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div/div/div[1]/a/div[2]")
    QUERY = (By.XPATH, "/html/body/div[3]/div[1]/div/div")
    FIRST_PICTURE = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img")
    PICTURE = (By.CSS_SELECTOR, ".MMImage-Origin")
    BUTTON_NEXT = (By.CSS_SELECTOR, ".CircleButton_type_next")
    BUTTON_PREVIOUS = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    