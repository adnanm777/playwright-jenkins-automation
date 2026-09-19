from playwright.sync_api import Page, expect


class AdminPage:

    def __init__(self, page: Page):
        self.page = page

        self.username_input = page.locator(
            "input[placeholder='Type for hints...']"
        )

        self.search_button = page.get_by_role(
            "button",
            name="Search"
        )

    def enter_username(self, username):
        self.username_input.fill(username)

    def click_search(self):
        self.search_button.click()

    def verify_username(self, username):
        expect(
            self.page.get_by_text(username, exact=True)
        ).to_be_visible()