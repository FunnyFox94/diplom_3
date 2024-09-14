import allure

from utils import urls as url

@allure.feature('Сброс пароля')
class TestResetPassword:
    @allure.story('Сценарий сброса пароля')
    @allure.title('Проверка функциональности сброса пароля')
    def test_reset_password_scenario(self, reset_password_page, login_page):
        with allure.step('Переход на страницу входа'):
            login_page.go_to_url(url.LOGIN_PAGE_URL)
            login_page.wait_for_loading_login_page()
        with allure.step('Переход на страницу сброса пароля'):
            login_page.click_reset_password_on_login_page()
            reset_password_page.wait_for_loading_reset_password_page()
        with allure.step('Проверка URL страницы сброса пароля'):
            assert reset_password_page.get_url() == url.FORGOT_PASSWORD_URL
        with allure.step('Ввод email для сброса пароля'):
            reset_password_page.enter_email_to_reset_password_field('momo@gmail.com')
        with allure.step('Клик по кнопке сброса пароля'):
            reset_password_page.click_reset_button_on_reset_button_page()
            reset_password_page.wait_for_loading_visibility_toggle()
        with allure.step('Проверка URL страницы после отправки формы'):
            assert reset_password_page.get_url() == url.RESET_PASSWORD_URL
        with allure.step('Клик по переключателю видимости пароля'):
            reset_password_page.click_on_visibility_toggle()
            reset_password_page.wait_for_change_focus_status_on_reset_password_field()
