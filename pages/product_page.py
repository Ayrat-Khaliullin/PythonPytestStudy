from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_added_to_cart(self, expected_product_name, expected_price):
        self.should_be_success_message()
        self.should_be_correct_product_name(expected_product_name)
        self.should_be_correct_price(expected_price)

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE), \
            "Product wasn't added to the cart"

    def should_be_correct_price(self, expected_price):
        product_price = self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
        assert product_price == expected_price, \
            f"cart total expected to be {expected_price} but was: {product_price}"

    def should_be_correct_product_name(self, expected_product_name):
        product_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert product_name == expected_product_name, \
            f"Product name in success message expected to be {expected_product_name} but was: {product_name}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE), "guest can see " \
                                                                                                "success message (" \
                                                                                                "expected that don't)"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_SUCCESS_MESSAGE), "success message didn't " \
                                                                                        "disappear"

