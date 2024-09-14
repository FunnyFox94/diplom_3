from selenium.webdriver.common.by import By

class LocatorsFeedPage:
    LATEST_ORDER_IN_ORDER_FEED = (By.XPATH, "//div/ul/li[1]/a/div/p[1]")
    ORDER_IN_PROGRESS = (By.XPATH, "//div/div/div/ul[2]/li")
    ORDERS_FOR_ALL_TIME = (By.XPATH, "//main/div/div/div/div[2]/p[2]")
    ORDERS_FOR_TODAY = (By.XPATH, "//main/div/div/div/div[3]/p[2]")
