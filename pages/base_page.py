from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """
    Класс, описывающий базовую страницу
    """
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """
        Базовый метод для открытия нужносй страницы
        """
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Базовый метод проверки наличия элемента на странице
        :param how: как искать по ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :param what: имя ID, CSS_SELECTOR, XPATH, CLASS_NAME
        :return: True - елемент найден на странице
                 False -элемент не найден
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
