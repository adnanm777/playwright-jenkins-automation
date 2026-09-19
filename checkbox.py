from playwright.sync_api import Page, expect


def test_checked(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")


    sunday_checkbox = page.get_by_label("Sunday")
    sunday_checkbox.check()

    expect(sunday_checkbox).to_be_checked()


    days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday","Friday","Saturday"]

    checkboxes = []
    for day in days:
        checkbox = page.get_by_label(day)
        checkboxes.append(checkbox) 

        print(f"Total number of checkboxes found: {len(checkboxes)}")

