import pytest
from config.config import base_url
from utils.logger import get_logger

from selenium import webdriver

# @pytest.fixture() # open browser, run one test, close browser. repeat
@pytest.fixture(scope="session") # open browser once, run all tests, close browser
def setup():
    driver=webdriver.Chrome()
    logger = get_logger()

    logger.info("Browser Opened")
    driver.get(base_url)
    driver.maximize_window()
    
    yield driver
    logger.info("Browser Closed")
    driver.quit()

    
