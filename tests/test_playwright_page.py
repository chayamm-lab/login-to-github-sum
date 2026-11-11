from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_playwright_page(driver):
    driver.get("https://playwright.dev/")
    driver.find_element(By.ID, "username")
    driver.find_elements(By.TAG_NAME, "input")
    my_elements = driver.find_elements(By.TAG_NAME)
    # element 
    # print(len(

def test_pw_css(driver):
    driver.set_window_size(800, 800)          # below Docusaurus's 997px breakpoint
    driver.get("https://www.playwright.dev")


    button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Toggle navigation bar"]')
    button.click()
    
    # cliLink = driver.find_element(By.XPATH, '//*[@class=".theme-layout-navbar.navbar.navbar--fixed-top"]/div[3]/div[2]/div[1]/ul/li[3]/a')
    cliLink = driver.find_element(By.XPATH, '//*[@id="__docusaurus"]/nav/div[3]/div[2]/div[1]/ul/li[3]/a')
    # cliLink = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div[3]/div[2]/div[1]/ul/li[3]/a')
    cliLink.click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://playwright.dev/agent-cli/introduction"))
    assert driver.current_url == "https://playwright.dev/agent-cli/introduction"