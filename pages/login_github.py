from playwright.sync_api import Locator, Page



from pages.base_page import BasePage
from utilities import config
import re




class LoginPage(BasePage):
    PATH = config.GITHUB_URL


    def __init__(self, page: Page):
        super().__init__(page)

    @property
    def sign_in_button(self) -> Locator:
        return self.page.get_by_role("link", name="Sign in")

    @property
    def email_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Username or email address")

    @property
    def password_field(self) -> Locator:
        return self.page.get_by_role("textbox", name="Password")    

    @property
    def sign_in_with_credentials(self) -> Locator:
        return self.page.get_by_role("button", name="Sign in", exact=True)
    
    
    def click_on_sign_in_button(self):
        self.sign_in_button.click()
        self.page.wait_for_url("**/login")
