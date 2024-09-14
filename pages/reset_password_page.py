import allure

from pages.base_page import BasePage
from locators.locators_reset_password_page import LocatorsResetPasswordPage as locatorResetPasswordPage


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод email "{email}" в поле для сброса пароля')
    def enter_email_to_reset_password_field(self, email):
        self.send_text_to_field(locatorResetPasswordPage.RESET_PASSWORD_FIELD, email)

    @allure.step('Клик по кнопке сброса пароля')
    def click_reset_button_on_reset_button_page(self):
        self.click_element(locatorResetPasswordPage.RESET_PASSWORD_BUTTON)

    @allure.step('Ожидание загрузки переключателя видимости пароля')
    def wait_for_loading_visibility_toggle(self):
        self.element_is_visible(locatorResetPasswordPage.TOGGLE_VISIBLE_PASSWORD)

    @allure.step('Клик по переключателю видимости пароля')
    def click_on_visibility_toggle(self):
        self.click_element(locatorResetPasswordPage.TOGGLE_VISIBLE_PASSWORD)

    @allure.step('Ожидание изменения фокуса на поле сброса пароля')
    def wait_for_change_focus_status_on_reset_password_field(self):
        self.element_is_visible(locatorResetPasswordPage.FOCUSED_RESET_PASSWORD_FIELD)

    @allure.step('Ожидание загрузки страницы сброса пароля')
    def wait_for_loading_reset_password_page(self):
        self.element_is_visible(locatorResetPasswordPage.RESET_PASSWORD_FIELD)
