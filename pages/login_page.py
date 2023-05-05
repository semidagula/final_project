from locators.login_locators import LogareClientInregistratLocators
from pages.base_page import BasePage
import time

from pages.home_page_page import Homepage


class LoginPage(BasePage):
    def navigate_to_website(self):
        self.driver.find_element

    def logare(self):
        self.driver.find_element(*LogareClientInregistratLocators.LOGARE).click()

    def insert_email(self, email):
        self.driver.find_element(*LogareClientInregistratLocators.ADRESA_EMAIL).send_keys(email)

    def insert_password(self, password):
        self.driver.find_element(*LogareClientInregistratLocators.PAROLA).send_keys(password)

    def login_button(self):
        self.driver.find_element(*LogareClientInregistratLocators.LOGIN_BUTTON).click()

    def check_wrong_email_login_error_message(self, expected_error_message):
        self.driver.find_element(*LogareClientInregistratLocators.EMAIL_ERROR_MESSAGE, expected_error_message)

    def check_wrong_password_login_error_message(self, expected_error_message):
        self.driver.find_element(*LogareClientInregistratLocators.PASSWORD_ERROR_MESSAGE, expected_error_message)
