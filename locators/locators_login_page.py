from selenium.webdriver.common.by import By

class LocatorsLoginPage:
    ENTER_POINT_TO_RESET_PASSWORD_PAGE = (By.XPATH, ".//a[contains(text(),'Восстановить пароль')]")
    EMAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    ENTER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]")
