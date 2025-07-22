import allure
from locators.order_feed_locators import LocatorsOrder
from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Получаем значение выполнено за все время")
    def get_value_completed_for_all_time(self):
        self.wait_for_element_text_not_empty(LocatorsOrder.ORDERS_TODAY)
        return self.get_text(LocatorsOrder.ORDERS_TODAY)

    @allure.step("Получаем значение выполнено за сегодня")
    def get_value_completed_for_today(self):
        self.wait_for_element_text_not_empty(LocatorsOrder.ORDERS_TODAY)
        return self.get_text(LocatorsOrder.ORDERS_TODAY)

    @allure.step("Получаем значение из списка заказов в работе")
    def get_value_orders_in_work(self):
        self.wait_for_element_text_not_empty(LocatorsOrder.ORDER_NUMBER)
        return self.get_text(LocatorsOrder.ORDER_NUMBER)

    @allure.step("Ждем чтобы заказ отобразился в заказах в работе")
    def wait_for_order_will_become_in_work(self):
        return self.wait_for_element_invisible(LocatorsOrder.ORDER_NUMBER)