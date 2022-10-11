from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
def verify_Email_field(context):
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