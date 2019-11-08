from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    """
    Класс, описывающий страницу продукта
    """
    def should_be_successful_add_product_in_basket(self):
        """
        Метод проверки корректного добавления товара в корзину
        """
        self.should_be_successful_message()
        self.should_be_product_name_in_successful_message()
        self.should_be_basket_price()

    def add_product_to_basket(self):
        """
        Метод добавления выбранного товара в корзину
        """
        basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        basket_button.click()

    def should_be_successful_message(self):
        """
        Метод проверки отображения сообщения
        о добавлении выбранного товара в корзину
        """
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME_MESSAGE
        ), "There is no message on the page"

    def should_be_product_name_in_successful_message(self):
        """
        Метод проверки наличия названия выбранного продукта
        в сообщении об успешном добавлении в корзину
        """
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text
        product_name_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_MESSAGE
        ).text

        assert product_name in product_name_message, \
            "the name of the product in the message does not match the name of the added product"

    def should_be_basket_price(self):
        """
        Метод проверки соответствия суммы в корзине
        цене выбранного товара
        """
        product_prise = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text
        basket_price = self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE
        ).text

        assert product_prise == basket_price, "Different prices"
