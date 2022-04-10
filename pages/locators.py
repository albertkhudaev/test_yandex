from selenium.webdriver.common.by import By


class MainPageLocators():
    SEARCH_BOX = (By.CSS_SELECTOR, "input#text")
    SUGGESTIONS = (By.CSS_SELECTOR, "body > div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile")
    SEARCH_RESULT = (By.CSS_SELECTOR, "#search-result")
    FIRST_RESULT = (By.XPATH, "//*[@id=\"search-result\"]/li[1]/div/div[1]/div[2]/div[1]/a/b")