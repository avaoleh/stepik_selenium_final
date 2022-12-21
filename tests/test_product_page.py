import time

import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage
from selenium.webdriver.common.by import By

links = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
]

@pytest.mark.parametrize('product_link', links)
def test_guest_can_add_product_to_basket(browser, product_link):
    link = product_link
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()