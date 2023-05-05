from locators.cautare_prod_locators import CautareProdus
from pages.base_page import BasePage


class SearchPage(BasePage):
    def click_search_bar(self):
        self.driver.find_element(*CautareProdus.SEARCH_BAR).click()

    def enter_product(self, product):
        self.driver.find_element(*CautareProdus.SEARCH_BAR).sendKeys(product)

    def click_search_button(self):
        self.driver.find_element(*CautareProdus.ADAUGARE_IN_COS).click()

    def select_product(self):
        self.driver.find_element(*CautareProdus.PANTOFI_SPORT).click()

    def select_number(self):
        self.driver.find_element(*CautareProdus.MARIMEA).click()

    def add_cart(self):
        self.driver.find_element(*CautareProdus.ADD_CART).click()

    def complete_the_order(self):
        self.driver.find_element(*CautareProdus.FINALIZARE_COMANDA).click()

    def conf_page(self):
        return self.driver.find_element(*CautareProdus.TEXT_FINALIZARE).is_displayed()

    def no_prod(self, nonexistent_product):
        self.driver.find_element(*CautareProdus.SEARCH_BAR).sendKeys(nonexistent_product)
        return self.driver.find_element(*CautareProdus.ERROR_MSG).is_displayed()
