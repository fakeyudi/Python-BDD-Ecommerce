import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


scenarios('../Features/loginModal.feature')


@given(u'Launch Firefox browser')
def open_firefox(context):
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(10)


@when(u'Flipkart home page opens')
def launch_flipkart(context):
    context.driver.get("https://www.flipkart.com/")
    assert True


@then(u'Verify Login Text is Present')
def verify_login(context):
    assert context.driver.find_element(By.CLASS_NAME, "_36KMOx").find_element(By.TAG_NAME, "span").text == "Login"


@then(u'Verify Email field is Present')
def verify_email_field(context):
    assert context.driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").is_displayed()


@then(u'Verify Password field is Present')
def verify_password_field(context):
    assert context.driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").is_displayed()


@then(u'Verify Login Button is Present')
def verify_login_button(context):
    assert context.driver.find_element("xpath", "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").is_displayed()


@then(u'Verify Close Button is Present')
def verify_close_button(context):
    assert context.driver.find_element("xpath", "/html/body/div[2]/div/div/button").is_displayed()


@then(u'Click Close Button')
def click_close_button(context):
    context.driver.find_element("xpath", "/html/body/div[2]/div/div/button").click()


@then(u'Close Browser')
def step_impl(context):
    context.driver.quit()


@then(u'Click on first phone')
def click_first_phone(context):
    context.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[4]/div/div[1]/a/div/img[2]").click()


@then(u'Verify Filters')
def verify_filters(context):
    assert context.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[1]/div/div/span").text == "Filters"


@then(u'Reset price to 20000')
def reset_price(context):
    select = Select(context.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[2]/div[4]/div[3]/select"))
    select.select_by_visible_text("₹30000+")


@then(u'Verify Need help')
def verify_need_help(context):
    context.driver.find_element("tag name", "body").send_keys(Keys.END)
    elem = context.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div[2]/a/div[1]/span")
    assert elem.location_once_scrolled_into_view
    assert elem.text == "Need help?"


@then(u'Verify Top Categories is present')
def verify_top_categories(context):
    assert context.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div").is_displayed()
    print(context.driver.find_element(By.CLASS_NAME, "_37M3Pb").find_elements(By.XPATH,"//div/a/div[2]"))


@then(u'Click Mobiles')
def click_mobiles(context):
    context.driver.find_element("xpath", "/html/body/div/div/div[2]/div/div/div[2]/a/div[2]").click()