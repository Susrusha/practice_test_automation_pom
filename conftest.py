import pytest
from config.config import base_url

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# @pytest.fixture(scope="module") # open browser once, run all tests, close browser
@pytest.fixture() # open browser, run one test, close browser. repeat
def setup():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    print("Browser opened")
    driver.get(base_url)
    driver.maximize_window()
    yield driver
    print("Browser closed")
    driver.quit()

    
