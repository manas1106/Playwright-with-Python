from playwright.sync_api import sync_playwright
import pytest
import time

with sync_playwright() as playwright:  #if you are using with open then no need to give 
    browser = playwright.chromium.launch(headless=False, slow_mo=4000, args=["--start-maximized"])
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")
    page.evaluate("window.scroll(0,1500)")
    time.sleep(2)

    #get_by_label is a locator in playwright 
    #get_by_label -> it takes the lable name as argument
    heading = page.get_by_text("with faded secondary text", exact=True) 
    heading.highlight()
    time.sleep(5)

    print("URL of page is: ", page.url)
    print("title of page is:", page.title())
    print("test of heading:", heading.text_content())
