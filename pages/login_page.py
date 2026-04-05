from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    # locators
    username_input = (By.ID, "username")
    password_input = (By.NAME,"password")
    submit_button = (By.ID,"submit")
    logout_link = (By.LINK_TEXT, "Log out")
    error_message = (By.ID, "error")
    # actions
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)
    
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
    # logic
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit()
    # validations
    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.logout_link)).click()

    def get_error_message(self):
        return WebDriverWait(self.driver,10).until(
        EC.visibility_of_element_located(self.error_message)).text
    
    