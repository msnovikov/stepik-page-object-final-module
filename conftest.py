import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Обработчик для задания браузера и языка браузера из командной строки"""
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    """Объявление выбранного браузера с выбранным языком"""
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        language_setting = Options()
        language_setting.add_experimental_option("prefs", {"intl.accept_languages": user_language})
        browser = webdriver.Chrome(options=language_setting)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test...")
        language_setting = webdriver.FirefoxProfile()
        language_setting.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=language_setting)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser")
    browser.quit()
