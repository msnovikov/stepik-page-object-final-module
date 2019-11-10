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
        self.should_be_success_message()
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

    def should_be_success_message(self):
        """
        Метод проверки отображения сообщения
        о добавлении выбранного товара в корзину
        """
        assert self.is_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "There is no message on the page"

    def should_not_be_success_message(self):
        """
        Метод проверки отсутствия сообщения об успешном
        добавлении товара в корзину
        """
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_be_success_message_disappeared(self):
        """
        Метод проверки того, что сообщение о добавлении
        товара в корзину исчезает
        """
        assert self.is_element_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message has not disappeared"

    def should_be_product_name_in_successful_message(self):
        """
        Метод проверки наличия названия выбранного продукта
        в сообщении об успешном добавлении в корзину
        """
        product_name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        product_name_message = self.get_element_text(*ProductPageLocators.PRODUCT_NAME_MESSAGE)

        assert product_name == product_name_message, \
            "the name of the product in the message does not match the name of the added product"

    def should_be_basket_price(self):
        """
        Метод проверки соответствия суммы в корзине и
        цены выбранного товара
        """
        product_prise = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        basket_price = self.get_element_text(*ProductPageLocators.BASKET_PRICE)

        assert product_prise == basket_price, "Different prices"
