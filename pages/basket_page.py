from .base_page import BasePage
from .locators import BasketPageLocators

EMPTY_BASKET_MESSAGES = {
    "en": "Your basket is empty.",
    "ru": "Ваша корзина пуста.",
    "fr": "Votre panier est vide.",
    "es": "Tu carrito esta vacío.",
}

class BasketPage(BasePage):
    def basket_should_be_empty(self, empty_message):
        cart_content = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT)
        content_text = cart_content.text.strip()
        assert content_text[0] in empty_message, f"Expected result: {empty_message}, actual result: {content_text}"