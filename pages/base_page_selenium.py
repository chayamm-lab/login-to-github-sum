from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait

Locator = tuple[str, str]


class SeleniumBasePage:
    PATH = "/"
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver: WebDriver, timeout: float = DEFAULT_TIMEOUT) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self) -> None:
        self.driver.get(self.PATH)
