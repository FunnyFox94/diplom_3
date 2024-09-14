import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_feed_page import LocatorsFeedPage
from pages.base_page import BasePage


def normalize_order_id(order_id):
    return order_id.lstrip('0')


class FeedPage(BasePage):
    @allure.step('Получение номера заказа в разделе "В работе"')
    def order_id_in_progress(self):
        return self.find_element(LocatorsFeedPage.ORDER_IN_PROGRESS).text

    @allure.step('Ожидание появления нового заказа с ID')
    def wait_for_id_new_order(self, order_id):
        order_id_locator = LocatorsFeedPage.ORDER_IN_PROGRESS
        WebDriverWait(self.driver, self.timeout).until(
            lambda driver: normalize_order_id(self.find_element(order_id_locator).text) == normalize_order_id(str(order_id))
        )

    @allure.step('Получение номера последнего заказа в ленте заказов')
    def order_id_in_latest_orders(self):
        return self.find_element(LocatorsFeedPage.LATEST_ORDER_IN_ORDER_FEED).text

    @allure.step('Получение количества заказов за сегодня')
    def get_orders_for_today(self):
        return self.find_element(LocatorsFeedPage.ORDERS_FOR_TODAY).text

    @allure.step('Получение общего количества заказов за все время')
    def get_orders_for_all_time(self):
        return self.find_element(LocatorsFeedPage.ORDERS_FOR_ALL_TIME).text
