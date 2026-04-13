from utils.logger import get_logger

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger()
    # locators
    username_input = (By.ID, "username")
    password_input = (By.NAME,"password")
    submit_button = (By.ID,"submit")
    logout_link = (By.LINK_TEXT, "Log out")
    error_message = (By.ID, "error")
    # actions
    def enter_username(self, username):
        self.logger.info("Entering username")
        self.logger.debug(f"Locator used: {self.username_input}")
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.logger.info("Entering password")
        self.logger.debug(f"Locator used: {self.password_input}")
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_submit(self):
        self.logger.info("Clicking submit button")
        self.logger.debug(f"Locator used: {self.submit_button}")
        self.driver.find_element(*self.submit_button).click()
    # logic
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
    # validations
    def click_logout(self):
        self.logger.info("Clicking logout button")
        self.logger.debug(f"Locator used: {self.logout_link}")
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.logout_link)).click()

    def get_error_message(self):
        self.logger.info("Finding error message")
        self.logger.debug(f"Locator used: {self.error_message}")
        return WebDriverWait(self.driver,10).until(
        EC.visibility_of_element_located(self.error_message)).text
    
    