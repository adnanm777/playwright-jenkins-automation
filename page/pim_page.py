from playwright.sync_api import Page, expect


class PimPage:

    def __init__(self, page: Page):
        self.page = page

        self.pim_heading = page.get_by_role(
            "heading",
            name="PIM"
        )

        self.add_button = page.get_by_role(
            "button",
            name="Add"
        )

        self.first_name = page.get_by_placeholder("First Name")
        self.middle_name = page.get_by_placeholder("Middle Name")
        self.last_name = page.get_by_placeholder("Last Name")

        self.save_button = page.get_by_role(
            "button",
            name="Save"
        )

    def verify_pim_page(self):
        expect(self.pim_heading).to_be_visible()

    def click_add(self):
        self.add_button.click()

    def enter_employee_name(self, first_name, middle_name, last_name):
        self.first_name.fill(first_name)
        self.middle_name.fill(middle_name)
        self.last_name.fill(last_name)

    def click_save(self):
        self.save_button.click()
