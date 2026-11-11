import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = Options()
    ciEnv =os.getenv("CI")
    print(f"Driver: {driver}")
    if ciEnv:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome()    
    yield driver
    driver.quit()  # runs even if the test fails