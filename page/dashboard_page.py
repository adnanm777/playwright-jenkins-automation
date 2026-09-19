from playwright.sync_api import Page, expect


class DashboardPage:

    def __init__(self, page: Page):
        self.page = page

        self.dashboard_link = page.get_by_role(
            "link",
            name="Dashboard"
        )

        self.admin_link = page.get_by_role(
            "link",
            name="Admin"
        )

        self.pim_link = page.get_by_role(
            "link",
            name="PIM"
        )

        self.leave_link = page.get_by_role(
            "link",
            name="Leave"
        )

        self.time_link = page.get_by_role(
            "link",
            name="Time"
        )

    def verify_dashboard(self):
        expect(
            self.dashboard_link
        ).to_be_visible()

    def click_dashboard(self):
        self.dashboard_link.click()

    def click_admin(self):
        self.admin_link.click()

    def click_pim(self):
        self.pim_link.click()

    def click_leave(self):
        self.leave_link.click()

    def click_time(self):
        self.time_link.click()