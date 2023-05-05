from behave import *
from pages.base_page import BasePage
from pages.login_page import LoginPage


@given("Login Page: I am on the shein boutique login page")
def step_given_on_login_page(context):

    context.base_page = BasePage(context.driver)
    context.base_page.navigate_to_url()
    context.login_page = LoginPage(context.driver)
    context.login_page.logare()



@when('Login Page: I insert  email "{email}" and I insert password "{password}"')
def step_impl(context, email, password):
    context.login_page.insert_email(email)
    context.login_page.insert_password(password)


@when('Login Page: I click the login button')
def step_impl(context):
    context.login_page.login_button()


@then('I can login into the application and see the list of product')
def step_impl(context):
    context.login_page.URL()


@then('Login Page: I cannot login into the application and I receive error message "{error_message}"')
def step_impl(context):
    error_message = "Introduceți o adresă de e-mail corectă. De exemplu ionpopescu@domeniu.ro."
    assert context.login_page.check_wrong_email_login_error_message == error_message
    error_msg = "Please enter more characters or clean leading or trailing spaces."
    assert context.login_page.check_wrong_password_login_error_message == error_msg
