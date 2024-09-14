import allure

from utils import urls as url
from utils.helpers import login_and_navigate_to_profile


@allure.feature('Навигация в личном кабинете')
class TestNavigationInPersonalCabinet:
    @allure.story('Переходы в личном кабинете и выход из аккаунта')
    @allure.title('Проверка навигации в личном кабинете пользователя')
    def test_personal_cabinet_navigation(self, driver, login_page, main_page, user_profile_page):
        with allure.step('Авторизация и переход на главную страницу'):
            login_and_navigate_to_profile(login_page, main_page)
        with allure.step('Ожидание загрузки кнопки аккаунта и переход в личный кабинет'):
            main_page.wait_for_account_button_loading()
            main_page.click_account_button()
        with allure.step('Ожидание загрузки страницы профиля'):
            user_profile_page.wait_for_loading_user_profile_page()
        with allure.step('Проверка URL страницы профиля'):
            assert user_profile_page.get_url() == url.ACCOUNT_PROFILE
        with allure.step('Выход из аккаунта'):
            user_profile_page.click_logout_button()
        with allure.step('Ожидание загрузки страницы логина'):
            login_page.wait_for_loading_login_page()
        with allure.step('Проверка URL страницы логина'):
            assert login_page.get_url() == url.LOGIN_PAGE_URL

