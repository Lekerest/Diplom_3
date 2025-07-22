from selenium.webdriver.common.by import By

class LocatorsLogin:

    # Поле email
    FIELD_EMAIL = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default']/*[text()='Email']/following-sibling::input")

    # Поле пароль
    FIELD_PASSWORD = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_password input_size_default']/*[text()='Пароль']/following-sibling::input")

    #Кнопка входа
    BUTTON_ENTRANCE = (By.CSS_SELECTOR, "button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")