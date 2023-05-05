from selenium.webdriver.common.by import By


class LogareClientInregistratLocators:
    LOGIN_BUTTON = (By.XPATH, '//*[@title="Logare"]')
    ADRESA_EMAIL = (By.XPATH, '//*[@id="email"]')
    PAROLA = (By.XPATH, '//*[@id="pass"]')
    LOGARE = (By.CSS_SELECTOR, "button[id='send2'] span span")
    REMEMBER_ME = (By.CSS_SELECTOR, "#remember_me3m2PWKipYZ")
    CAMP_OBLIGATORIU = (By.ID, 'advice-required-entry-pass')
    FORGOT_PASSWORD = (By.CSS_SELECTOR, '.f-left')
    EMAIL_ERROR_MESSAGE = (By.CSS_SELECTOR, "#advice-validate-email-email")
    PASSWORD_ERROR_MESSAGE = (By.CSS_SELECTOR, "#advice-validate-password-pass")