from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента {locator}')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу {locator}')
    def click_element(self, locator):
        return self.find_element(locator).click()

    @allure.step('Перетаскивание элемента {source_locator} в элемент {target_locator}')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step("Перетаскивание элемента через JS из {source_locator} в {target_locator}")
    def drag_and_drop_js(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)

        js = """
          function simulateDragDrop(sourceNode, destinationNode) {
              var EVENT_TYPES = {
                  DRAG_END: 'dragend',
                  DRAG_START: 'dragstart',
                  DROP: 'drop'
              };

              function createCustomEvent(type) {
                  var event = new CustomEvent("CustomEvent");
                  event.initCustomEvent(type, true, true, null);
                  event.dataTransfer = {
                      data: {},
                      setData: function(type, val) {
                          this.data[type] = val;
                      },
                      getData: function(type) {
                          return this.data[type];
                      }
                  };
                  return event;
              }

              function dispatchEvent(node, type, event) {
                  if (node.dispatchEvent) {
                      return node.dispatchEvent(event);
                  }
                  if (node.fireEvent) {
                      return node.fireEvent("on" + type, event);
                  }
              }

              var dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START);
              dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent);

              var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
              dropEvent.dataTransfer = dragStartEvent.dataTransfer;
              dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);

              var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
              dragEndEvent.dataTransfer = dragStartEvent.dataTransfer;
              dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
          }

          simulateDragDrop(arguments[0], arguments[1]);
          """
        self.driver.execute_script(js, source, target)

    # @allure.step('Ввод значения в элемент {locator}')
    # def send_keys_to_element(self, locator, value):
    #     return self.find_element(locator).send_keys(value)
    #
    # @allure.step('Скролл к элементу {locator}')
    # def scroll_to(self, locator):
    #     element = self.find_element(locator)
    #     return self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #
    # @allure.step('Переход к элементу {locator}')
    # def scroll_to_element(self, locator):
    #     return self.scroll_to(locator)
    #

    @allure.step('Ожидание изменения URL с {old_url}')
    def wait_for_url_change(self, old_url, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.url_changes(old_url))

    @allure.step('Переключение на последнюю вкладку')
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получить ссылку')
    def get_url(self):
        self.switch_to_last_window()
        self.wait_for_url_change('about:blank')
        return self.driver.current_url

    @allure.step('Ожидание отображения элемента {locator}')
    def wait_for_element_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидание исчезновения элемента {locator}')
    def wait_for_element_invisible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Проверка, отображается ли элемент {locator}')
    def is_element_displayed(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('Получить текст элемента {locator}')
    def get_text(self, locator):
        text = self.find_element(locator).text
        try:
            return int(text)
        except ValueError:
            return text

    @allure.step('Ожидание изменения текста элемента {locator}')
    def wait_for_text_change(self, locator, old_text, timeout=5):
        WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(*locator).text != old_text)


