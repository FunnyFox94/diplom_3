import allure

from utils import urls as url
from utils.helpers import login_and_create_order

@allure.feature('Создание заказа')
class TestCreatingOrder:
    @allure.story('Отображение номера заказа в разделе "В работе"')
    @allure.title('Проверка, что номер заказа отображается в разделе "В работе"')
    def test_order_number_appears_in_progress_section(self, main_page, login_page, feed_page):
        with allure.step('Авторизация и создание заказа'):
            login_and_create_order(login_page, main_page)
            order_id = int(main_page.order_id())
        with allure.step('Переход на страницу ленты заказов и ожидание нового заказа'):
            feed_page.go_to_url(url.FEED)
            feed_page.wait_for_id_new_order(order_id)
        feed_page.go_to_url(url.FEED)
        feed_page.wait_for_id_new_order(order_id)

        with allure.step('Получение номера заказа из раздела "В работе"'):
            order_id_in_progress_section = int(feed_page.order_id_in_progress())
        with allure.step('Сравнение ожидаемого и фактического номера заказа'):
            assert order_id == order_id_in_progress_section

    @allure.story('История заказов в ленте заказов')
    @allure.title('Проверка отображения истории заказов в ленте заказов')
    def test_order_history_displays_in_order_feed(self, main_page, login_page, feed_page, user_profile_page):
        with allure.step('Авторизация и создание заказа'):
            login_and_create_order(login_page, main_page)
            order_id = main_page.order_id()  # Почему делаю это в двух тестах. Я проверяю, что в in progress летит нужный id
        with allure.step('Переход на страницу ленты заказов и ожидание нового заказа'):
            feed_page.go_to_url(url.FEED)
            feed_page.wait_for_id_new_order(order_id)
            latest_order_id = feed_page.order_id_in_latest_orders()
        with allure.step('Переход в профиль пользователя'):
            main_page.click_account_button()
            user_profile_page.wait_for_loading_user_profile_page()
        with allure.step('Проверка истории заказов в профиле пользователя'):
            user_profile_page.click_order_history_link()
            latest_order_id_in_user_profile = user_profile_page.latest_order_in_user_profile()
        with allure.step('Сравнение номеров последних заказов'):
            assert latest_order_id == latest_order_id_in_user_profile

    @allure.story('Изменение счетчиков заказов в ленте заказов')
    @allure.title('Проверка изменения счетчиков заказов после создания нового заказа')
    def test_check_order_counters_change_in_order_feed(self, main_page, login_page, feed_page):
        with allure.step('Получение текущих значений счетчиков заказов'):
            feed_page.go_to_url(url.FEED)
            old_orders_for_today = feed_page.get_orders_for_today()
            old_orders_for_all_time = feed_page.get_orders_for_all_time()
        with allure.step('Авторизация и создание нового заказа'):
            login_and_create_order(login_page, main_page)
        with allure.step('Обновление счетчиков заказов'):
            feed_page.go_to_url(url.FEED)
            new_orders_for_today = feed_page.get_orders_for_today()
            new_orders_for_all_time = feed_page.get_orders_for_all_time()
        with allure.step('Проверка изменения счетчиков заказов'):
            assert old_orders_for_today != new_orders_for_today
            assert old_orders_for_all_time != new_orders_for_all_time
