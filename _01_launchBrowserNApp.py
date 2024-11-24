from playwright.sync_api import sync_playwright
import pytest


with sync_playwright() as playwright:
    #this will launch chrome by default
    #browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    # Launch Edge browser instead of chrome
    browser = playwright.chromium.launch(channel="msedge", headless=False, slow_mo=4000)
    page = browser.new_page()

    page.goto("https://playwright.dev/")

    print("You're on:", page.title())
    #get_by_role is a locator in playwright 
    getStarted_button = page.get_by_role('link', name='GET STARTED')

    getStarted_button.click()
    print("URL of getting started page is: ", page.url)

    browser.close()

