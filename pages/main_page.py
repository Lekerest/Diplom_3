import allure
from locators.base_page_locators import LocatorsGeneral
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик по кнопке 'Лента заказов'")
    def click_on_order_feed(self):
        return self.click_element(LocatorsGeneral.BUTTON_ORDER_FEED)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_button_constructor(self):
        return self.click_element(LocatorsGeneral.BUTTON_CONSTRUCTOR)

    @allure.step("Клик по ингредиенту 'Пурпурная булка'")
    def click_on_ingredient_purple_bulka(self):
        return self.click_element(LocatorsGeneral.INGREDIENT_PURPLE_BULKA)

    @allure.step("Проверка отображения кнопки 'Закрыть информацию'")
    def is_close_button_visible(self):
        return self.is_element_displayed(LocatorsGeneral.BUTTON_CLOSE_INFO)

    @allure.step("Клик по крестику в информации к ингредиенту'")
    def click_on_cross(self):
        return self.click_element(LocatorsGeneral.BUTTON_CLOSE_INFO)

    @allure.step('Ожидание исчезновения кнопки закрытия окна информации')
    def wait_until_close_button_disappears(self):
        return self.wait_for_element_invisible(LocatorsGeneral.BUTTON_CLOSE_INFO)

    @allure.step('Перетаскивание ингредиента фиолетовая булка в конструктор')
    def drag_ingredient_purple_bulka_to_constructor(self, ingredient_locator=LocatorsGeneral.INGREDIENT_PURPLE_BULKA,
                                       constructor_locator=LocatorsGeneral.CONSTRUCTOR_AREA):
        self.drag_and_drop(ingredient_locator, constructor_locator)

    allure.step('Перетаскивание ингредиента в конструктор (альтернативный метод)')

    @allure.step("Перетаскивание ингредиента в конструктор через JS")
    def drag_ingredient_to_constructor_js(self):
        self.drag_and_drop_js(LocatorsGeneral.INGREDIENT_PURPLE_BULKA, LocatorsGeneral.CONSTRUCTOR_AREA)

    @allure.step('Получить текущее значение счетчика фиолетовой булки')
    def get_counter_value_purple_bulka(self):
        return self.get_text(LocatorsGeneral.COUNTER_PURPLE_BULKA)

    def wait_until_counter_changes(self, old_value):
        self.wait_for_text_change(LocatorsGeneral.COUNTER_PURPLE_BULKA, str(old_value))