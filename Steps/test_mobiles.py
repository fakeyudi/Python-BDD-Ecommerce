from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


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