from playwright.sync_api import sync_playwright
import pytest
import time

with sync_playwright() as playwright:  #if you are using with open then no need to give 
    browser = playwright.chromium.launch(headless=False, slow_mo=4000, args=["--start-maximized"])
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")
    page.evaluate("window.scroll(0,3500)")
    time.sleep(2)

    #get_by_label is a locator in playwright 
    #get_by_label -> it takes the lable name as argument
    email_input = page.get_by_label("Email address", exact=True) #exact=true with this playwright will return an exception is more than one "Email address" found
    email_input.highlight()
    time.sleep(5)

    #get_by_placeholder takes the name of placeholder as an argument
    password_input = page.get_by_placeholder("Password") 
    password_input.highlight()
    time.sleep(5)

    example_select = page.get_by_label("Example select")
    example_select.highlight()
    time.sleep(5)

    print("URL of page is: ", page.url)
    print("title of page is:", page.title())
