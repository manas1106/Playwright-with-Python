from playwright.sync_api import sync_playwright
import pytest

#it's not running Need to investigate 
@pytest.mark.parametrize("browser_type", ["chromium", "firefox", "webkit"])

def test_launch_different_browsers(browser_type):
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_type).launch(headless=False, slow_mo=3000)
        page = browser.new_page()

        page.goto("https://google.com")

        print("You're on:", page.title())
        #get_by_role is a locator in playwright 
        #getStarted_button = page.get_by_role('link', name='GET STARTED')

        #getStarted_button.click()
        print("URL of the page is: ", page.url)

        browser.close()
