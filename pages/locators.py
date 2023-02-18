from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default' and (contains(@href,'/basket/'))]")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'product_main')]//h1")
    PRICE = (By.CLASS_NAME, "price_color")
    ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_ADDED_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class,'alertinner') and contains(.,'был добавлен в "
                                               "вашу корзину')]")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.XPATH, "//div[contains(@class,'alertinner') and contains(.,'был добавлен в вашу "
                                              "корзину')]//strong ")
    CART_TOTAL = (By.XPATH, "//div[contains(@class,'alertinner') and contains(.,'Стоимость корзины теперь "
                            "составляет')]//strong ")


class BasketPageLocators:
    EMPTY_MESSAGE = (By.XPATH, "//div[@id='content_inner' and (contains(.,'Your basket is empty') or (contains(.,"
                               "'Ваша корзина пуста')))]")
    PRODUCTS_LIST = (By.CSS_SELECTOR, '.basket-items')
