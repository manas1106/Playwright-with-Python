from playwright.sync_api import sync_playwright
import pytest
import time

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=4000,)
    # Launch Edge browser instead of Chromium
    #browser = playwright.msedge.launch(headless=False, slow_mo=4000)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")
    #get_by_role is a locator in playwright 
    #get_by_role by button
    defaultButton = page.get_by_role('button', name='Default button')
    defaultButton.click()

    #get_by_role by heading
    #page.set_viewport_size({"width": 1920, "height": 1000})
    page.evaluate("window.scroll(0,1500)")
    heading2 = page.get_by_role('heading', name='Heading 2')

    defaultButton.highlight()
    time.sleep(5)
    heading2.highlight()
    time.sleep(2)
    print("URL of page is: ", page.url)
    browser.close()
