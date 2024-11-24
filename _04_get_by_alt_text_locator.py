from playwright.sync_api import sync_playwright
import pytest
import time

with sync_playwright() as playwright:  #if you are using with open then no need to give 
    browser = playwright.chromium.launch(headless=False, slow_mo=4000)
    page = browser.new_page()

    page.goto("https://google.com")
    #page.evaluate("window.scroll(0,1500)")

    image_txt = page.get_by_alt_text("Google") #used to locate images in case if image is not loaded, so img can be located with img text
    image_txt.highlight()
    time.sleep(5)

    print("URL of page is: ", page.url)
    print("title of page is:", page.title())