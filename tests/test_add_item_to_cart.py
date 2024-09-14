import allure

from utils import urls as url
from utils.helpers import login_and_navigate_to_profile

@allure.feature('Корзина')
class TestAddItemToCart:
    @allure.story('Добавление товара в корзину')
    @allure.title('Проверка добавления товара в корзину')
    def test_add_item_to_cart(self, main_page, login_page):
        with allure.step('Авторизация и переход в профиль'):
            login_and_navigate_to_profile(login_page, main_page)
            main_page.go_to_url(url.LOGIN_PAGE_URL)

        with allure.step('Переход на главную страницу'):
            main_page.click_constructor_in_header()
            main_page.wait_for_loading_cards_content()
            assert main_page.get_url() == url.BASE_URL

        with allure.step('Добавление товара в корзину'):
            main_page.drag_item_to_cart()
            main_page.wait_for_counter_change()

        with allure.step('Проверка, что товар добавлен в корзину'):
            assert main_page.total_order_price() > 0

    @allure.story('Открытие карточки товара')
    @allure.title('Проверка открытия и закрытия карточки товара')
    def test_open_item_cart(self, main_page, login_page):
        with allure.step('Авторизация и переход в профиль'):
            login_and_navigate_to_profile(login_page, main_page)
            main_page.go_to_url(url.BASE_URL)

        with allure.step('Открытие карточки товара'):
            main_page.wait_for_loading_cart_area()
            main_page.click_item_card()
            main_page.wait_for_open_card()

        with allure.step('Закрытие карточки товара'):
            main_page.click_close_modal_button()
            main_page.wait_for_loading_cart_area()
        with allure.step('Проверка, что карточка товара закрыта'):
            assert main_page.close_modal_button_is_not_visible() == True
