import allure
from locators.login_locators import LocatorsLogin
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Ввод email")
    def input_email(self):
        return self.send_keys_to_element(LocatorsLogin.FIELD_EMAIL, "Ivan_Hritankov_123@ya.ru")

    @allure.step("Ввод password")
    def input_password(self):
        return self.send_keys_to_element(LocatorsLogin.FIELD_PASSWORD, "test123qweasdzxcvfr")

    @allure.step("Клик по кнопке войти")
    def click_on_button_entrance(self):
        return self.click_element(LocatorsLogin.BUTTON_ENTRANCE)