from selenium.webdriver.common.by import By

class LocatorsGeneral:

    BUTTON_CONSTRUCTOR = (By.CSS_SELECTOR, '.AppHeader_header__linkText__3q_va.ml-2')

    BUTTON_ORDER_FEED = (By.XPATH, ".//*[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Лента Заказов']")

    INGREDIENT_PURPLE_BULKA = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__text__yp3dH")

    BUTTON_CLOSE_INFO = (By.CSS_SELECTOR, ".Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")

    CONSTRUCTOR_AREA =  (By.CSS_SELECTOR, ".BurgerConstructor_basket__list__l9dp_")

    COUNTER_PURPLE_BULKA = (By.CSS_SELECTOR, ".counter_counter__num__3nue1")

    BUTTON_ORDER_CREATE = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg")

    ORDER_NUMBER = (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")

    BLOCK = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")
