import time

from behave import *

from pages.cautare_prod_page import SearchPage
from pages.home_page_page import Homepage


@given(u'user visits the website')
def step_impl(context):
    context.home_page = Homepage(context.home_page.driver)
    context.home_page.open()
    time.sleep(3)


@when(u'I click the search bar')
def step_impl(context):
    context.search_page = SearchPage(context.search_page.driver)
    context.search_page.click_search_bar()


@when(u'I enter product "{product}"')
def step_impl(context, product):
    context.search_page.enter_product(product)


@when(u'I click the search button')
def step_impl(context):
    context.search_page.click_search_button()


@then(u'I select the product "{product}"')
def step_impl(context):
    context.search_page.select_product()


@then(u'I select the number "{number}"')
def select_number(context, number):
    context.search_page.select_number(number)


@then('I click on the add to cart button')
def add_cart(context):
    context.search_page.add_cart()


@then('I click on complete order button')
def complete_order(context):
    context.search_page.complete_the_order()


@then('I see a successful message displayed')
def conf_order(context):
    message =  context.search_page.conf_page()
    assert message == 'FINALIZARE COMANDĂ'


@when('I enter nonexistent_product "{product}"')
def step_when_user_performs_nonexistent_search(context):
    context.search_page.no_prod()


@then
def step_then_search_result_message_should_appear(context):

    message = context.search.no_prod()
    assert message == "Căutarea dvs. nu a returnat niciun rezultat."
