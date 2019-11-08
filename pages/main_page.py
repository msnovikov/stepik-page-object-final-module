from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    """
    Класс, описывающий главную страницу
    """
    def go_to_login_page(self):
        """
        Метод для перехода на страницу логина с главной страницы
        """
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        """
        Метод проверки наличия ссылки на страницу
        логина/регистрации на главной странице
        """
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
