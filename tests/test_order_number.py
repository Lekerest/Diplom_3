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
