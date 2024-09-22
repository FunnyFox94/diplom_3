import allure
import pytest
from selenium import webdriver

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from pages.user_profile_page import UserProfilePage
from utils import urls as url


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def login_page(driver):
    return LoginPage(driver)

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def user_profile_page(driver):
    return UserProfilePage(driver)

@pytest.fixture
def reset_password_page(driver):
    return ResetPasswordPage(driver)

@pytest.fixture
def feed_page(driver):
    return FeedPage(driver)

@allure.step("Авторизоваться")
@pytest.fixture
def login_and_navigate_to_profile(login_page, main_page):
    login_page.go_to_url(url.LOGIN_PAGE_URL)
    login_page.wait_for_loading_login_page()
    login_page.auth_on_login_page()

    main_page.wait_for_account_button_loading()
    main_page.click_account_button()
    return main_page

@allure.step("Авторизоваться и создать заказ")
@pytest.fixture
def login_and_create_order(login_and_navigate_to_profile, main_page):
    main_page.go_to_url(url.BASE_URL)
    main_page.click_constructor_in_header()
    main_page.wait_for_loading_cards_content()
    main_page.drag_item_to_cart()
    main_page.click_order_button()
    main_page.wait_for_loading_modal_after_order()
    main_page.close_modal_after_order()
    return main_page

