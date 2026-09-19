from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        self.username = page.locator(
            "input[name='username']"
        )

        self.password = page.locator(
            "input[name='password']"
        )

        self.login_button = page.locator(
            "button[type='submit']"
        )

    def enter_username(self, username):
        self.username.fill(username)

    def enter_password(self, password):
        self.password.fill(password)

    def click_login(self):
        self.login_button.click()