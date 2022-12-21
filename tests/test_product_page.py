import uuid

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.urls import PromoLinks
from pages.basket_page import EMPTY_BASKET_MESSAGES
import time # в начале файла


link_ = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
pages_list = [f'{link_}?promo=offer{i}' for i in range(10)]
pages_list[7] = pytest.param(pages_list[7], marks=pytest.mark.xfail(reason='bugged'))

link_product = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"


@pytest.mark.logged_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
        self.browser = browser

        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"

        login_page = LoginPage(browser, login_link)
        login_page.open()
        email, password = f"{uuid.uuid4().hex}@fakemail.com", uuid.uuid4().hex
        login_page.register_new_user(email, password)

    @pytest.mark.need_review
    def test_user_cant_see_success_massage(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, self.link)
        page.open()
        page.add_product_to_basket()


# @pytest.mark.parametrize('link', PromoLinks.promo_list)
@pytest.mark.parametrize('link', pages_list)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_into_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = link_product
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = link_product
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, user_language):
    link = link_product
    page = ProductPage(browser, link)
    page.open()
    page.open_basket()
    basket_page = BasketPage(browser, browser.current_url)
    expected_message = EMPTY_BASKET_MESSAGES[user_language]
    basket_page.basket_should_be_empty(expected_message)
