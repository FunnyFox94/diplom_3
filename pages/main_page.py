import allure
from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from locators.locators_main_page import LocatorsMainPage


class MainPage(BasePage):
    @allure.step('Клик по кнопке аккаунта')
    def click_account_button(self):
        self.click_element(LocatorsMainPage.ACCOUNT_BUTTON_ON_MAIN_PAGE)

    @allure.step('Ожидание загрузки кнопки аккаунта')
    def wait_for_account_button_loading(self):
        self.element_is_visible(LocatorsMainPage.ACCOUNT_BUTTON_ON_MAIN_PAGE)

    @allure.step('Клик по карточке товара')
    def click_item_card(self):
        self.click_element(LocatorsMainPage.ITEM_CARD)

    @allure.step('Клик по конструктору в хедере')
    def click_constructor_in_header(self):
        self.click_element(LocatorsMainPage.CONSTRUCTOR_BUTTON)

    @allure.step('Ожидание загрузки карточек товаров')
    def wait_for_loading_cards_content(self):
        self.element_is_visible(LocatorsMainPage.ITEM_CARD)

    @allure.step('Ожидание открытия карточки товара')
    def wait_for_open_card(self):
        self.element_is_visible(LocatorsMainPage.CLOSE_MODAL_BUTTON)

    @allure.step('Клик по кнопке закрытия модального окна')
    def click_close_modal_button(self):
        self.click_element(LocatorsMainPage.CLOSE_MODAL_BUTTON)

    @allure.step('Перетаскивание товара в корзину')
    def drag_item_to_cart(self):
        cart = self.find_element(LocatorsMainPage.CART_AREA)
        item = self.find_element(LocatorsMainPage.ITEM_CARD)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(item, cart).perform()

    @allure.step('Ожидание изменения счетчика товаров')
    def wait_for_counter_change(self):
        self.element_is_visible(LocatorsMainPage.CHANGED_ITEM_COUNTER)

    @allure.step('Ожидание загрузки области корзины')
    def wait_for_loading_cart_area(self):
        self.element_is_visible(LocatorsMainPage.CART_AREA)

    @allure.step('Проверка видимости кнопки закрытия модального окна')
    def close_modal_button_is_not_visible(self):
        return self.is_element_not_present(LocatorsMainPage.CLOSE_MODAL_BUTTON)

    @allure.step('Получение общей стоимости заказа')
    def total_order_price(self):
        return int(self.find_element(LocatorsMainPage.TOTAL_PRICE_COUNT).text)

    @allure.step('Клик по кнопке оформления заказа')
    def click_order_button(self):
        self.click_element(LocatorsMainPage.CREATE_ORDER_BUTTON)

    @allure.step('Ожидание загрузки модального окна после заказа')
    def wait_for_loading_modal_after_order(self):
        self.element_is_not_visible(LocatorsMainPage.WAIT_CLOSE_OVERLAY)

    @allure.step('Закрытие модального окна после заказа')
    def close_modal_after_order(self):
        self.click_element(LocatorsMainPage.CLOSE_MODAL_BUTTON)

    @allure.step('Получение идентификатора заказа')
    def order_id(self):
        return self.find_element(LocatorsMainPage.ORDER_ID).text
