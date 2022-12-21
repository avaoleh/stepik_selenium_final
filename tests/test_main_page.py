from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.basket_page import EMPTY_BASKET_MESSAGES

link_main_page = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    link = link_main_page
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, user_language):
    link = link_main_page
    page = MainPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    expected_message = EMPTY_BASKET_MESSAGES[user_language]
    basket_page.basket_should_be_empty(expected_message)