import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    ciEnv =os.getenv("CI")
    if ciEnv:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome() 
    print(f"Driver: {driver}")   
    yield driver
    driver.quit()  # runs even if the test fails