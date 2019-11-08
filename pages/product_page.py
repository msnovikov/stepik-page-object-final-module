from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Класс, описывающий страницу продукта
    """
    def add_product_to_basket(self):
        """
        Метод добавления выбранного товара в корзину
        """
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
