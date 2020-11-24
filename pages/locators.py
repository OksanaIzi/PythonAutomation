from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1)")
    BASKET_BOOKNAME = (By.CSS_SELECTOR, ".alert:nth-child(1) >div > strong")
    MAIN_BOOKNAME = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main > p")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert:nth-child(3) > div > p > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")