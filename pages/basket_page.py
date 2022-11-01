from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), "Basket is not empty"

    def should_be_empty_basket_text(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text \
               == "Your basket is empty. Continue shopping", "Message of empty basket not found"
