"""
Тест-кейсы для страницы продукта
"""
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    """
    Тест добавления выбранного товара в корзину
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

# реализовать проверки ожидаемого результата для теста добавления товара в корзину
