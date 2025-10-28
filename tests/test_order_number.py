import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from helpers import HelpersFunctions


class TestOrderFeedCounters:

    @allure.title("Проверка увеличения счётчика 'Выполнено за сегодня'")
    @allure.description("После создания заказа счётчик 'Выполнено за сегодня' должен увеличиться")
    @pytest.mark.parametrize("driver", [
        {"browser": "chrome", "start": 2},
        {"browser": "firefox", "start": 2}
    ], indirect=True)
    def test_order_today_counter_increment(self, driver):
        driver, order_today, _, _ = HelpersFunctions.user_with_order_data(driver)
        order_page = OrderFeedPage(driver)

        new_order_today = order_page.get_value_completed_for_today()

        with allure.step("Проверка, что счётчик увеличился"):
            assert new_order_today == order_today + 1, (
                f"Ожидалось, что значение 'Выполнено за сегодня' увеличится. "
                f"Было: {order_today}, стало: {new_order_today}"
            )

    @allure.title("Проверка увеличения счётчика 'Выполнено за все время")
    @allure.description("После создания заказа счётчик 'Выполнено за все время' должен увеличиться")
    @pytest.mark.parametrize("driver", [
        {"browser": "chrome", "start": 2},
        {"browser": "firefox", "start": 2}
    ], indirect=True)
    def test_order_today_counter_increment(self, driver):
        driver, _, order_all_time, _ = HelpersFunctions.user_with_order_data(driver)
        order_page = OrderFeedPage(driver)

        new_order_all_time = order_page.get_value_completed_for_all_time

        with allure.step("Проверка, что счётчик увеличился"):
            assert new_order_all_time == order_all_time + 1, (
                f"Ожидалось, что значение 'Выполнено за сегодня' увеличится. "
                f"Было: {order_all_time}, стало: {new_order_all_time}"
            )

    @allure.title("Проверка что номер заказа попадает в блок в работе ")
    @allure.description("После создания заказа заказ должен попасть в блок в работе")
    @pytest.mark.parametrize("driver", [
        {"browser": "chrome", "start": 2},
        {"browser": "firefox", "start": 2}
    ], indirect=True)
    def test_order_today_counter_increment(self, driver):
        driver, _, _, order_number = HelpersFunctions.user_with_order_data(driver)
        order_page = OrderFeedPage(driver)
        order_page.wait_for_order_will_become_in_work()
        new_order_number = order_page.get_value_orders_in_work()
        assert order_number == new_order_number
