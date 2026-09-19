from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    # 1. Launch browser
    browser = p.chromium.launch(headless=False)

    # 2. Create page
    page = browser.new_page()

    # 3. Open website
    page.goto("https://demo.automationtesting.in/Register.html")

    # 4. First Name
    page.get_by_placeholder("First Name").fill("Mohammad Adnan")

    # 5. Last Name
    page.get_by_placeholder("Last Name").fill("Khan")

    # 6. Address
    page.locator("textarea").fill(
        "Near kgn kirana shop akber plot akola"
    )

    # 7. Email
    page.locator("input[type='email']").fill(
        "mohammadadnan.khan@gmail.com"
    )

    # 8. Phone
    page.locator("input[type='tel']").fill("1234567890")

    # 9. Gender
    page.locator("input[value='Male']").check()

    # 10. Hobbies
    page.locator("input[value='Cricket']").check()

     # 12. Languages dropdown
    page.locator("#msdd").click()
    
    page.locator("li:has-text('English')").click()

    # 11. Skills dropdown
    page.locator("#Skills").select_option("Analytics")


    page.locator("li:has-text('English')").click()

    print("Test case executed successfully")

    page.wait_for_timeout(5000)

    browser.close()