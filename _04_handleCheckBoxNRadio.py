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
    #get_by_role by radio
    #page.evaluate("window.scroll(0,3000)")
    radio = page.get_by_role('radio', name='Option two can be something else and selecting it will deselect option one')
    #radio.highlight() --it worked but highlighted intentionally
    #time.sleep(5)  --it worked but highlighted intentionally
    radio.click()  ##it will also work similarly with radio.check()
    time.sleep(5)

    #Handle Checkbox
    defaultCheckbox = page.get_by_role('checkbox', name='Default checkbox')

    #defaultCheckbox.highlight()
    #time.sleep(5)
    defaultCheckbox.check()
    time.sleep(5)  #if checkbox is already checked then .check() will do nothing 
    defaultCheckbox.uncheck()  #if checkbox is already Unchecked then .uncheck() will do nothing
    time.sleep(5)
    print("URL of page is: ", page.url)
    browser.close()
