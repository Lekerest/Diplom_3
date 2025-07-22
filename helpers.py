import time

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class HelpersFunctions:

    def user_with_order_data(driver):
        """
        Авторизация, переход в ленту заказов, получение данных и создание заказа.
        Возвращает: (driver, orders_today, orders_all_time, order_now)
        """
        login_page = LoginPage(driver)
        login_page.input_email()
        login_page.input_password()
        login_page.click_on_button_entrance()

        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        #Даже с этим ожиданием в мазиле тест падает.
        main_page.wait_for_order_feed_button_clickable()
        main_page.click_on_order_feed()

        orders_today = order_page.get_value_completed_for_today()
        orders_all_time = order_page.get_value_completed_for_all_time

        main_page.wait_for_constructor_button_clickable()
        main_page.click_on_button_constructor()

        main_page.wait_for_counter_purple_bulka_clickable()
        main_page.drag_ingredient_to_constructor_js()
        main_page.click_on_order_button()
        main_page.wait_for_order_number_visible()
        time.sleep(5)
        order_now = main_page.get_order_number()
        main_page.click_on_cross()
        main_page.click_on_order_feed()

        return driver, orders_today, orders_all_time, order_now
