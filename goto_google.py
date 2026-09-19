from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")
        page.wait_for_timeout(5000)
        browser.close()


if __name__ == "__main__":
    main()
