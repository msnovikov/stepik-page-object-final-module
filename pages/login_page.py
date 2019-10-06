from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        try:
            "login" in self.browser.current_url
        except:
            assert False
        assert True

    def should_be_login_form(self):
        try:
            self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        except NoSuchElementException:
            assert False, "Login form is not presented"
        assert True

    def should_be_register_form(self):
        try:
            self.is_element_present(*LoginPageLocators.REGISTER_FORM)
        except NoSuchElementException:
            assert False, "Register form is not presented"
        assert True
