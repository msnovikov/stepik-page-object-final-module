from .pages.main_page import MainPage


def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open_page()
    page.go_to_login_page()
