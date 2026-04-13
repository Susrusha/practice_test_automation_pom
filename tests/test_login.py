import random
import string
import pytest

from utils.logger import get_logger
from pages.login_page import LoginPage
from config.config import base_url, redirected_url

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.valid
def test_valid_details(setup):
    driver=setup
    login_page = LoginPage(driver)
    logger = get_logger()
    logger.info("Start test: Valid login") 
    login_page.login("student", "Password123")
    login_page.click_logout()
    WebDriverWait(driver, 5).until(EC.url_contains(base_url))
    assert driver.current_url==base_url

@pytest.mark.invalid
def test_invalid_details(setup):
    driver=setup
    login_page = LoginPage(driver)
    logger = get_logger()
    logger.info("Start test: Invalid login") 
    username = ''.join(random.choices(string.ascii_letters, k=7))
    print("username: ",username)
    login_page.login(username, "Password123")
    assert login_page.get_error_message() == "Your username is invalid!"
    
def test_blank(setup):
    driver = setup
    login_page = LoginPage(driver)
    logger = get_logger()
    logger.info("Start test: Blank login") 
    login_page.click_submit()
    assert login_page.get_error_message() == "Your username is invalid!"

@pytest.mark.redirect
def test_page_redirecting(setup):
    driver=setup
    login_page = LoginPage(driver)
    logger = get_logger()
    logger.info("Start test: Page redirecting") 
    login_page.login("student", "Password123")
    WebDriverWait(driver, 5).until(EC.url_to_be(redirected_url))
    assert driver.current_url==redirected_url
