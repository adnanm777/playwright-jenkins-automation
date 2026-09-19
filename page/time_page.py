from playwright.sync_api import Page, expect


class TimePage:

    def __init__(self, page: Page):
        self.page = page

        self.time_heading = page.get_by_role(
            "heading",
            name="Time",
            exact=True
        )

    def verify_time_page(self):
        expect(
            self.time_heading
        ).to_be_visible()