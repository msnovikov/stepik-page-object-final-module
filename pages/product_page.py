from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
