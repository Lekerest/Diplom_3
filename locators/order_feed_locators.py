from selenium.webdriver.common.by import By

class LocatorsOrder:

    ORDERS_TODAY = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня:')]/following-sibling::p")

    ORDERS_ALL_TIME = (By.CSS_SELECTOR, ".OrderFeed_number__2MbrQ.text.text_type_digits-large")

    ORDER_NUMBER = (By.XPATH, "(//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]//li)[1]")