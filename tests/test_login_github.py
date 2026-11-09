from playwright.sync_api import Page, expect
from pages.login_github import LoginPage
from utilities.config import TEST_EMAIL_GITHUB, TEST_PASSWORD_GITHUB

def test_sign_in_to_gmail(page: Page):
    sign_in_page = LoginPage(page)
    sign_in_page.open() 
   
    page.pause()
    
    sign_in_page.click_on_sign_in_button()
    
    

    assert TEST_EMAIL_GITHUB is not None
    assert TEST_PASSWORD_GITHUB is not None
    
    sign_in_page.email_field.fill(TEST_EMAIL_GITHUB)
    sign_in_page.password_field.fill(TEST_PASSWORD_GITHUB)
    
    expect(sign_in_page.sign_in_with_credentials).to_be_visible()

   
    pass
