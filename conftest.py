import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="choose browser 'chrome' or 'firefox'")
    parser.addoption("--language", action="store", default="en",
                     help="choose language ru or en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    user_language = request.config.getoption("--language")
    if browser_name == "chrome":
        print("\nstart chrome for test..")
        options = ChOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart chrome for test..")
        options = Options()
        options.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(options=options)

    else:
        pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nclose browser for test..")
    browser.quit()
