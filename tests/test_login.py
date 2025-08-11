import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/login.feature")

@pytest.fixture
def driver():
    gridUrl = "hub.lambdatest.com/wd/hub"
    username = "paulocol"
    accessKey = "8Yl2j4huUuLPcQIkt54LrxujI0Of43g1vZaSAbBiCi8FRMdi7Y"

    lt_options = {
        "user": username,
        "accessKey": accessKey,
        "build": "Python BDD Build",
        "name": "Test Case X",
        "platformName": "Windows 11",
        "w3c": True,
        "browserName": "Chrome",
        "browserVersion": "latest",
        "selenium_version": "latest"
    }


    web_driver = webdriver.ChromeOptions()

    options = web_driver
    options.set_capability('LT:Options', lt_options)


    url = f"https://{username}:{accessKey}@{gridUrl}"
   
    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
   
    driver.quit

@given("the user is on the login screen")
def user_on_login_screen(driver):
    driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

@when("they enter valid login details")
def enter_valid_login_details(driver):
    driver.find_element(By.ID, "input-email").send_keys("lambdatestblogs@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("test123@")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']").click()

@then("the my account dashboard should appear")
def dashboard_should_appear(driver):
    header = driver.find_element(By.CSS_SELECTOR, "h2.card-header.h5")
    assert header.is_displayed()
    assert "route=account/account" in driver.current_url

@when(parsers.parse('the user logs in with "{username}" and "{password}"'))
def do_login(driver, username, password):
    driver.find_element(By.ID, "input-email").send_keys(username)
    driver.find_element(By.ID, "input-password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']").click()