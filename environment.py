from selenium import webdriver




def before_all(context):
    context.driver = webdriver.Chrome()

    yield context.driver
    context.driver.quit()



# Apoi, în codul unde este utilizat 'LoginPage':

