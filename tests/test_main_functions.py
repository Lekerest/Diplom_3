import allure
import pytest
from locators.base_page_locators import LocatorsGeneral
from pages.main_page import MainPage
from urls import Urls


class TestWebCrossing:

    @allure.title("Переход по кнопке 'Конструктор'")
    @allure.description("Проверка перехода на главную страницу при нажатии на кнопку 'Конструктор'")
    @pytest.mark.parametrize('driver',
        [
            {'browser': 'chrome', 'start': 2},
            {'browser': 'firefox', 'start': 2},
        ], indirect=True
    )
    def test_crossing(self, driver):
        web = MainPage(driver)
        web.click_on_button_constructor()
        with allure.step("Проверка, что URL после перехода совпадает с ожидаемым"):
            actual_url = web.get_url()
            assert actual_url == Urls.MAIN_PAGE, (
                f"Ожидался переход на {Urls.MAIN_PAGE}, но получен {actual_url}"
            )

    @allure.title("Открытие окна ингредиента при клике")
    @allure.description("Проверка, что при нажатии на ингредиент открывается окно с информацией")
    @pytest.mark.parametrize('driver',
        [
            {'browser': 'chrome', 'start': 1},
            {'browser': 'firefox', 'start': 1},
        ], indirect=True
    )
    def test_click_on_ingredient_open_info(self, driver):
        web = MainPage(driver)
        web.click_on_ingredient_purple_bulka()
        with allure.step("Проверка, что отображается кнопка закрытия информации"):
            is_displayed = web.is_element_displayed(LocatorsGeneral.BUTTON_CLOSE_INFO)
            assert is_displayed, "Кнопка закрытия информации не отображается при клике на ингредиент"

    @allure.title("Проверка отображения кнопки закрытия информации")
    @allure.description("Проверка, что при открытии информации об ингредиенте видна кнопка закрытия")
    @pytest.mark.parametrize('driver',
        [
            {'browser': 'chrome', 'start': 1},
            {'browser': 'firefox', 'start': 1},
        ], indirect=True
    )
    def test_click_on_ingredient_purple_bulka_open_info(self, driver):
        web = MainPage(driver)
        web.click_on_ingredient_purple_bulka()
        with allure.step("Проверка, что кнопка закрытия информации видима"):
            is_visible = web.is_close_button_visible()
            assert is_visible, "Кнопка закрытия информации не отображается"

    @allure.title("Закрытие окна информации по нажатию на крестик")
    @allure.description("Проверка, что окно информации закрывается по нажатию на крестик")
    @pytest.mark.parametrize('driver',
        [
            {'browser': 'chrome', 'start': 1},
            {'browser': 'firefox', 'start': 1},
        ], indirect=True
    )
    def test_click_on_cross_to_close(self, driver):
        web = MainPage(driver)
        web.click_on_ingredient_purple_bulka()
        web.click_on_cross()
        web.wait_until_close_button_disappears()
        with allure.step("Проверка, что окно информации закрыто"):
            is_still_visible = web.is_close_button_visible()
            assert not is_still_visible, "Окно информации не было закрыто после нажатия на крестик"

    @allure.title("Добавление ингредиента увеличивает счётчик")
    @allure.description("Проверка, что при добавлении ингредиента в конструктор счётчик увеличивается на 1")
    @pytest.mark.parametrize('driver',
        [
            {'browser': 'chrome', 'start': 1},
            {'browser': 'firefox', 'start': 1},
        ], indirect=True
    )
    def test_add_ingredient_increases_counter(self, driver):
        web = MainPage(driver)
        old_value = web.get_counter_value_purple_bulka()
        web.drag_ingredient_to_constructor_js()
        web.wait_until_counter_changes(old_value)
        new_value = web.get_counter_value_purple_bulka()
        with allure.step("Проверка, что счётчик увеличился на 1 после добавления ингредиента"):
            assert new_value == old_value + 2, (
                f"Ожидалось, что счётчик увеличится с {old_value} до {old_value + 2}, "
                f"но фактически: {new_value}"
            )
