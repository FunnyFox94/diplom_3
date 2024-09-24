import allure

from utils import urls as url


@allure.feature('Корзина')
class TestAddItemToCart:
    @allure.story('Добавление товара в корзину')
    @allure.title('Проверка добавления товара в корзину')
    def test_add_item_to_cart(self, main_page, login_page, login_and_navigate_to_profile):
        main_page.go_to_url(url.LOGIN_PAGE_URL)

        main_page.click_constructor_in_header()
        main_page.wait_for_loading_cards_content()
        assert main_page.get_url() == url.BASE_URL

        main_page.drag_item_to_cart()
        main_page.wait_for_counter_change()

        assert main_page.total_order_price() > 0

    @allure.story('Открытие карточки товара')
    @allure.title('Проверка открытия и закрытия карточки товара')
    def test_open_item_cart(self, main_page, login_page, login_and_navigate_to_profile):
        main_page.go_to_url(url.BASE_URL)

        main_page.wait_for_loading_cart_area()
        main_page.click_item_card()
        main_page.wait_for_open_card()

        main_page.click_close_modal_button()
        main_page.wait_for_loading_cart_area()
        assert main_page.close_modal_button_is_not_visible() is True
