from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class Homepage(BasePage):

    def open(self):
        self.driver.get(self.URL)

    def get_logo(self):
        return self.driver.find_element(*HomePageLocators.LOGO_HOME_PAGE).is_displayed()
