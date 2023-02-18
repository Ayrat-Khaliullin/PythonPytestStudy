from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "the message that basket is empty doesn't " \
                                                                           "present at the page"

    def should_not_have_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_LIST), "expected that basket is empty but has " \
                                                                               "a product"
