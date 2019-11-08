from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Элементы главной страницы
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    """
    Элементы страницы логина/регистрации
    """
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    """
    Элементы страницы товара
    """
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_MESSAGE = (By.CSS_SELECTOR, "#messages>.alert-success:nth-child(1)>.alertinner>strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info>.alertinner>p>strong")
