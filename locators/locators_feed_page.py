from selenium.webdriver.common.by import By

class LocatorsFeedPage:
    LATEST_ORDER_IN_ORDER_FEED = (By.XPATH, "//li[1]//a[contains(@class, 'OrderHistory')]/div/p[1]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'orderListReady')]/li")
    ORDERS_FOR_ALL_TIME = (By.XPATH, "//div[2]//p[contains(@class, 'digits-large')]")
    ORDERS_FOR_TODAY = (By.XPATH, "//div[3]//p[contains(@class, 'digits-large')]")
