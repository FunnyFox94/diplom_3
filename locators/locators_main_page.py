from selenium.webdriver.common.by import By

class LocatorsMainPage:
    ACCOUNT_BUTTON_ON_MAIN_PAGE = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    ORDER_FEED = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
    ITEM_CARD = (By.XPATH, "//section//ul[1]/a[1]")
    CART_AREA = (By.XPATH, ".//span[contains(text(), 'Перетяните булочку сюда (верх)')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, ".//section[contains(@class, 'opened')]//button")
    INITIAL_ITEM_COUNTER = (By.XPATH, ".//section//ul[1]/a[1]/div/p[contains(text(), '0')]")
    CHANGED_ITEM_COUNTER = (By.XPATH, ".//section//ul[1]/a[1]/div/p[contains(text(), '2')]")
    TOTAL_PRICE_COUNT = (By.XPATH, ".//section[contains(@class, 'basket')]/div/div/p")
    CREATE_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")
    CLOSE_MODAL_BUTTON_AFTER_ORDER = (By.XPATH, "//div[contains(@class, 'Modal')]//button")
    WAIT_CLOSE_OVERLAY = (By.XPATH, "//div[contains(@class, 'opened')]")
    ORDER_ID = (By.XPATH, "//div[contains(@class, 'Modal')]/h2")
