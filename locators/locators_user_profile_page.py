from selenium.webdriver.common.by import By

class LocatorsUserProfilePage:
    LOGOUT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Выход')]")
    LATEST_ORDER_ID = (By.XPATH, "//li[last()]/a/div/p[1]")
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
