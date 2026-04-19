import pytest
import allure
from config.config import base_url
from utils.logger import get_logger

from selenium import webdriver

# @pytest.fixture() # open browser, run one test, close browser. repeat
@pytest.fixture(scope="function")
def setup():
    driver=webdriver.Chrome()
    logger = get_logger()

    logger.info("Browser Opened")
    driver.get(base_url)
    driver.maximize_window()
    
    yield driver
    logger.info("Browser Closed")
    driver.quit()

# ----------- HOOK -----------------
@pytest.hookimpl(hookwrapper=True) # let test finish
def pytest_runtest_makereport(item, call): # run every test
    outcome = yield # pause
    result = outcome.get_result()
    # only when test fails in execution

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("setup")
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name = "Failed Screenshots",
                attachment_type = allure.attachment_type.PNG
            )


    
