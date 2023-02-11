from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote as RemoteWebDriver


class BasePage:

    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, by, value):
        try:
            self.browser.find_element(by, value)
        except NoSuchElementException:
            return False
        return True

    def get_current_url(self):
        self.browser.current_url
