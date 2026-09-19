from playwright.sync_api import Page, expect


def test_checked(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    male_radio = page.locator("#male")

    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()

    expect(male_radio).not_to_be_checked()

    male_radio.check()

    expect(male_radio).to_be_checked()

    page.wait_for_timeout(3000) 




    print("Test case executed successfully")