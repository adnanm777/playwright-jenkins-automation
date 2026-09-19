from playwright.sync_api import Page


class FailureAnalyzer:

    def __init__(self, page: Page):
        self.page = page

    def collect_page_evidence(self, error_message: str):

        evidence = {
            "url": self.page.url,
            "title": self.page.title(),
            "error": error_message,
            "dom": self.page.locator("body").inner_html(),
        }

        return evidence