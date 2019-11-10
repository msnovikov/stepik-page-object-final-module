from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    """
    Класс, описывающий страницу корзины
    """
    def should_be_basket_page(self):
        """
        Проверка страницы корзины:
        """
        self.should_be_basket_url()

    def should_be_basket_url(self):
        """
        Проверка наличия 'basket' в URL страницы корзины
        """
        assert "basket" in self.browser.current_url, "Not 'basket' in URL"

    def should_be_basket_text(self):
        """
        Метод проверки отображения текста о том,
        что корзина пуста
        """
        assert self.is_element_present(
            *BasketPageLocators.BASKET_TEXT
        ), "There is no text on the basket page"

    def should_not_be_basket_items(self):
        """
        Метод проверки отсутствия товаров в корзине
        """
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS
        ), "Basket items is presented, but should not be"
