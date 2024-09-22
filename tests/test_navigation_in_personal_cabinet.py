import allure

from utils import urls as url


@allure.feature('Навигация в личном кабинете')
class TestNavigationInPersonalCabinet:
    @allure.story('Переходы в личном кабинете и выход из аккаунта')
    @allure.title('Проверка навигации в личном кабинете пользователя')
    def test_personal_cabinet_navigation(self, login_page, main_page, user_profile_page, login_and_navigate_to_profile):
        main_page.wait_for_account_button_loading()
        main_page.click_account_button()
        user_profile_page.wait_for_loading_user_profile_page()
        with allure.step('Проверка URL страницы профиля'):
            assert user_profile_page.get_url() == url.ACCOUNT_PROFILE
        user_profile_page.click_logout_button()
        login_page.wait_for_loading_login_page()
        with allure.step('Проверка URL страницы логина'):
            assert login_page.get_url() == url.LOGIN_PAGE_URL
