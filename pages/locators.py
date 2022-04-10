from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_BOX = (By.CSS_SELECTOR, "input#text")
    SUGGESTIONS = (By.CSS_SELECTOR, "body > div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile")