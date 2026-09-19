from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    # 1. Launch browser
    browser = p.chromium.launch(headless=False)

    # 2. Create page
    page = browser.new_page()

    # 3. Open website
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

   page.type("name="username"","Admin")
    
    page.type("name="password"","admin123")
    page.click("type="submit"")

    page.wait_for_timeout(5000)



