from playwright.sync_api import sync_playwright
import pytest


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    # Launch Edge browser instead of Chromium
    #browser = playwright.msedge.launch(headless=False, slow_mo=4000)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")

    print("You're on:", page.title)

    print("URL of getting started page is: ", page.url)

    browser.close()
