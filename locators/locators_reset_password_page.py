from selenium.webdriver.common.by import By


class LocatorsResetPasswordPage:
    RESET_PASSWORD_FIELD = (By.XPATH, ".//input[@name='name']")
    TOGGLE_VISIBLE_PASSWORD = (By.XPATH, ".//div[@class='input__container']/div/div//*[name()='svg']")
    RESET_PASSWORD_BUTTON = (By.XPATH, ".//button[contains(text(),'Восстановить')]")
    DEFAULT_SIZE_RESET_PASSWORD_FIELD = (By.XPATH, ".//div[contains(@class, 'input_size_default')]")
    FOCUSED_RESET_PASSWORD_FIELD = (By.XPATH, ".//div[contains(@class, 'input_status_active')]")
