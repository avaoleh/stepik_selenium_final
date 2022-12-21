from .base_page import BasePage
from .locators import BasketPageLocators

EMPTY_BASKET_MESSAGES = {
    "en": "Your basket is empty.",
    "ru": "Ваша корзина пуста.",
    "fr": "Votre panier est vide.",
    "es": "Tu carrito esta vacío.",
    "de": "Ihr Warenkorb ist leer.",
    "it": "Il tuo carrello è vuoto.",
    "zh-cn": "Your basket is empty.",
}


class BasketPage(BasePage):
    def basket_should_be_empty(self, empty_message):
        cart_content = self.browser.find_element(*BasketPageLocators.Basket_CONTENT).text
        content_text = cart_content.text.strip()
        assert cart_content == empty_message, f"Expected result: {empty_message}, actual result: {content_text}"