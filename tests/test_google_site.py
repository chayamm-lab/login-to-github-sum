import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.selenium
def test_google_title(driver):
    driver.get("https://www.google.com")
    assert driver.title == "Google"
    

@pytest.mark.selenium
def test_google_search(driver):
    driver.get("https://www.google.com")
    search_field = driver.find_element(By.NAME, "q")
    # search_field = driver.find_element(By.CSS_SELECTOR, '[aria-label="חיפוש"]')
    search_field.send_keys("SOXL stock price")
    search_field.clear()
    print(f"Attribute: {search_field.get_attribute("name")}")
    # search_field.submit()
    search_field.send_keys(Keys.ENTER)
    
