import allure

from pages.base_page import BasePage
from locators.locators_user_profile_page import LocatorsUserProfilePage

class UserProfilePage(BasePage):
    @allure.step('Ожидание загрузки страницы профиля пользователя')
    def wait_for_loading_user_profile_page(self):
        self.element_is_visible(LocatorsUserProfilePage.LOGOUT_BUTTON)

    @allure.step('Клик по кнопке "Выйти"')
    def click_logout_button(self):
        self.click_element(LocatorsUserProfilePage.LOGOUT_BUTTON)

    @allure.step('Получение ID последнего заказа в профиле пользователя')
    def latest_order_in_user_profile(self):
        return self.find_element(LocatorsUserProfilePage.LATEST_ORDER_ID).text

    @allure.step('Клик по ссылке "История заказов"')
    def click_order_history_link(self):
        self.click_element(LocatorsUserProfilePage.ORDERS_HISTORY_LINK)
