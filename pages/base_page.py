import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage:
    """
    Класс, описывающий базовую страницу
    """
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        """
        Метод для перехода на страницу логина
        """
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket_page(self):
        """
        Метод перехода на страницу корзины
        """
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def get_element_text(self, how, what):
        """
        Базовый метод получения текста выбранного элемента
        :param how: как искать элемент: по ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param what: имя элемента: ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :return: элемент найден - возвращается текст элемента
                 элемент не найден - возвращается False
        """
        try:
            return self.browser.find_element(how, what).text
        except NoSuchElementException:
            return False

    def is_element_present(self, how, what):
        """
        Базовый метод проверки наличия элемента на странице
        :param how: как искать элемент: по ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param what: имя элемента: ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :return: True - елемент найден на странице
                 False -элемент не найден
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Базовый метод проверки того, что элемент не появляется на странице
        в течении заданного времени
        :param how: как искать элемент: по ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param what: имя элемента: ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param timeout: время явного ожидания
        :return: True - элемент не появился на странице
                 False - элемент появился на странице
        """
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((how, what))
            )
        except TimeoutException:
            return True

        return False

    def is_element_disappeared(self, how, what, timeout=4):
        """
        Базовый метод проверки того, что элемент исчезает мо страницы
        в течении заданного времени
        :param how: как искать элемент: по ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param what: имя элемента: ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param timeout: время явного ожидания
        :return: True - элемент исчез
                 False - элемент не исчез
        """
        try:
            WebDriverWait(
                self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_all_elements_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def open(self):
        """
        Базовый метод для открытия нужносй страницы
        """
        self.browser.get(self.url)

    def should_be_login_link(self):
        """
        Метод проверки наличия ссылки на страницу
        логина/регистрации на главной странице
        """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def solve_quiz_and_get_code(self):
        """
        Метод для ввода ответа в alert
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
