from playwright.sync_api import sync_playwright
import pytest
import time

with sync_playwright() as playwright:  #if you are using with open then no need to give 
    browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    page = browser.new_page()

    page.goto("https://bootswatch.com/default/")
    page.evaluate("window.scroll(0,1000)")
    time.sleep(2)

    # Commonly used Tag name, Class name, ID, and Attribute name
    #to use class name format- tag_name.class_name
    email_address = page.locator("input.form-control")  #this is not unique locator
    email_address.highlight()
    time.sleep(3)

    #has-text("") locator-> tag:has-text("")
    #email_address = page.locator("input:has-text('Email address')")
    #email_address.highlight()
    #time.sleep(3)

    # :nth-match(button.btn-primary,13) it is taking tag.class_name, and position of button
    large_Button = page.locator(":nth-match(button.btn-primary,13)")
    large_Button.highlight()
    time.sleep(3)

    #id can be used with # tag#id_name 
    password = page.locator("input#exampleInputPassword1")
    password.highlight()
    time.sleep(3)

    #Attribute name and value can be used with tag
    example_Select = page.locator("select[id='exampleSelect1']")
    example_Select.click()
    time.sleep(4)

    print("Title of page:", page.title())