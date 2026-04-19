from playwright.sync_api import sync_playwright
import time

def test_successful_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        time.sleep(5)
        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")
        page.locator("#login-button").click()

        assert "inventory" in page.url
        assert page.locator(".title").inner_text() == "Products"
        time.sleep(5)
        browser.close()



def test_invalid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator("#user-name").fill("wrong_user")
        page.locator("#password").fill("wrong_password")
        page.locator("#login-button").click()

        error_message = page.locator("[data-test='error']").inner_text()
        assert "Username and password do not match" in error_message
        time.sleep(5)
        browser.close()
