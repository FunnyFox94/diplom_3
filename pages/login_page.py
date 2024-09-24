import allure

from pages.base_page import BasePage
from locators.locators_login_page import LocatorsLoginPage as locatorLoginPage
import utils.test_data as data


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание загрузки страницы сброса пароля')
    def wait_for_loading_login_page(self): # по хорошему надо вынести это в отдельный page
        self.element_is_visible(locatorLoginPage.ENTER_POINT_TO_RESET_PASSWORD_PAGE)

    @allure.step('Клик по ссылке сброса пароля на странице логина')
    def click_reset_password_on_login_page(self): # по хорошему надо вынести это в отдельный page
        self.click_element(locatorLoginPage.ENTER_POINT_TO_RESET_PASSWORD_PAGE)

    @allure.step('Авторизация на странице логина с email')
    def auth_on_login_page(self):
        self.send_text_to_field(locatorLoginPage.EMAIL_FIELD, data.TEST_EMAIL)
        self.send_text_to_field(locatorLoginPage.PASSWORD_FIELD, data.TEST_PASSWORD)
        self.click_element(locatorLoginPage.ENTER_BUTTON)
