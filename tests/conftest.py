import pytest
from selenium import webdriver
from urls import Urls

@pytest.fixture()
def driver(request):
    # Ожидаем словарь с параметрами: browser и start
    params = getattr(request, 'param', {'browser': 'firefox', 'start': 1})
    browser = params.get('browser', 'firefox').lower()
    start = params.get('start', 1)

    # Инициализация драйвера
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Неподдерживаемый браузер: {browser}")

    driver.maximize_window()

    # Открытие нужной страницы
    if start == 1:
        driver.get(Urls.MAIN_PAGE)
    elif start == 2:
        driver.get(Urls.LOGIN_PAGE)
    else:
        raise ValueError(f"Неверный параметр start: {start}")

    yield driver
    driver.quit()
