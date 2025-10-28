import pytest
from selenium import webdriver
from urls import Urls
from pages.login_page import LoginPage


def _init_driver(browser: str):
    """Инициализация драйвера по имени браузера."""
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")
    driver.maximize_window()
    return driver


@pytest.fixture()
def driver(request):
    """
    Фикстура для инициализации WebDriver.
    request.param — словарь с ключами 'browser' и 'start'.
    """
    params = getattr(request, 'param', {'browser': 'firefox', 'start': 1})
    browser = params.get('browser', 'firefox').lower()
    start = params.get('start', 1)

    driver = _init_driver(browser)

    if start == 1:
        driver.get(Urls.MAIN_PAGE)
    elif start == 2:
        driver.get(Urls.LOGIN_PAGE)
    elif start == 3:
        driver.get(Urls.ORDER_FEED_PAGE)
    else:
        raise ValueError(f"Неверный параметр start: {start}")

    yield driver
    driver.quit()
