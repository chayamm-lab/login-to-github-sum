import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    print(f"Driver: {driver}")
    yield driver
    driver.quit()  # runs even if the test fails