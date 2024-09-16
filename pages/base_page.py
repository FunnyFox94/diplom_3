import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        self.element_is_active(locator)
        return element.click()

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def element_is_active(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))

    def element_is_not_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Получить URL страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Перейти на страницу')
    def go_to_url(self, page_url):
        return self.driver.get(page_url)

    def send_text_to_field(self, locator, text):
        element = self.find_element(locator)
        return element.send_keys(text)

    def is_element_not_present(self, locator):
        elements = self.driver.find_elements(*locator)
        return len(elements) == 0

    def wait_for_element_with_text(self, locator, expected_text, normalize_func=None):
        def condition(driver):
            element_text = self.find_element(locator).text
            if normalize_func:
                return normalize_func(element_text) == normalize_func(expected_text)
            else:
                return element_text == expected_text

        WebDriverWait(self.driver, self.timeout).until(condition)

    def wait_for_id_new_order(self, locator, order_id):
        self.wait_for_element_with_text(locator, str(order_id), self._normalize_order_id)

    def _normalize_order_id(self, order_id):
        return order_id.lstrip('0')
