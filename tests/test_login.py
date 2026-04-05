import random
import string

from pages.login_page import LoginPage
from config.config import base_url, redirected_url

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_details(setup):
    driver=setup
    login_page = LoginPage(driver)
    login_page.login("student", "Password123")
    login_page.click_logout()
    WebDriverWait(driver, 10).until(EC.url_contains(base_url))
    assert driver.current_url==base_url

def test_invalid_details(setup):
    driver=setup
    login_page = LoginPage(driver)
    username = ''.join(random.choices(string.ascii_letters, k=7))
    print("username: ",username)
    login_page.login(username, "Password123")
    assert login_page.get_error_message() == "Your username is invalid!"
    
def test_blank(setup):
    driver = setup
    login_page = LoginPage(driver)
    login_page.click_submit()
    assert login_page.get_error_message() == "Your username is invalid!"

def test_page_redirecting(setup):
    driver=setup
    login_page = LoginPage(driver)
    login_page.login("student", "Password123")
    WebDriverWait(driver,10).until(EC.url_to_be(redirected_url))
    assert driver.current_url==redirected_url
