import pytest
from selenium import webdriver

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage
from pages.user_profile_page import UserProfilePage


@pytest.fixture  #(scope='class')
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