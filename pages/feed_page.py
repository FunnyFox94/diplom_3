import allure

from locators.locators_feed_page import LocatorsFeedPage
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step('Получение номера заказа в разделе "В работе"')
    def order_id_in_progress(self):
        return self.find_element(LocatorsFeedPage.ORDER_IN_PROGRESS).text

    @allure.step('Получение номера последнего заказа в ленте заказов')
    def order_id_in_latest_orders(self):
        return self.find_element(LocatorsFeedPage.LATEST_ORDER_IN_ORDER_FEED).text

    @allure.step('Получение количества заказов за сегодня')
    def get_orders_for_today(self):
        return self.find_element(LocatorsFeedPage.ORDERS_FOR_TODAY).text

    @allure.step('Получение общего количества заказов за все время')
    def get_orders_for_all_time(self):
        return self.find_element(LocatorsFeedPage.ORDERS_FOR_ALL_TIME).text


    def wait_for_id_new_order(self, order_id):
        order_id_locator = LocatorsFeedPage.ORDER_IN_PROGRESS
        super().wait_for_id_new_order(order_id_locator, order_id)
