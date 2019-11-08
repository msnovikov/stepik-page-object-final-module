from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    """
    Класс, описывающий страницу логина/регистрации
    """
    def should_be_login_page(self):
        """
        Проверка страницы логина/регистрации
        """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """
        Проверка наличия 'login' в URL страницы логина/регистрации
        """
        assert "login" in self.browser.current_url, "Not 'login' in URL"

    def should_be_login_form(self):
        """
        Проверка наличия формы логина на странице логина/регистрации
        """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        """
                Проверка наличия формы регистрации на странице логина/регистрации
        """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
