from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def product_has_been_added_to_your_basket(self):
        actual_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        expected_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert expected_name == actual_name, f"actual name is {actual_name} but expected name is {expected_name}"

    def basket_price_is_equal_product_price(self):
        actual_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_AMOUNT).text
        expected_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert actual_price == expected_price, f"actual price is {actual_price} but expected price is {expected_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element didn't disappear"


