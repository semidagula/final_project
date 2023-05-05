class BasePage:
    def navigate_to_url(self):
        self.driver.get('https://shine-boutique.ro/')

    def __init__(self, driver):
        self.driver = driver

    def back(self):
        self.driver.back()
