from behave import *
from selenium.webdriver.common.by import By


@then(u'Verify Top Categories is present')
def verify_top_categories(context):
    assert context.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div").is_displayed()
    print(context.driver.find_element(By.CLASS_NAME, "_37M3Pb").find_elements(By.XPATH,"//div/a/div[2]"))


@then(u'Click Mobiles')
def click_mobiles(context):
    context.driver.find_element("xpath", "/html/body/div/div/div[2]/div/div/div[2]/a/div[2]").click()


# @then(u'Verify Mobiles page is displayed')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Verify Mobiles page is displayed')
