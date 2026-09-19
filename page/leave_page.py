from playwright.sync_api import Page, expect


class LeavePage:

    def __init__(self, page: Page):
        self.page = page

        self.leave_heading = page.get_by_role(
            "heading",
            name="Leave",
            exact=True
        )

    def verify_leave_page(self):
        expect(
            self.leave_heading
        ).to_be_visible()