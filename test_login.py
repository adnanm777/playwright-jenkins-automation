from playwright.sync_api import sync_playwright

from tests.conftest import page

def test_login(): 
    with sync_playwright() as p:
       
        browser = p.chromium.launch(headless=False)

        page.goto("https://google.com/")

        

