from playwright.sync_api import sync_playwright
import time

def test_open_saucedemo_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge" , headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        assert page.title() == "Swag Labs"
        time.sleep(10)
        browser.close()