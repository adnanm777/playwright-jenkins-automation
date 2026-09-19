from playwright.sync_api import sync_playwright
from healing.generic_locator_healer import GenericLocatorHealer
from healing.safe_ai_healer import SafeAIHealer


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()

    page.goto(
        "https://demowebshop.tricentis.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    broken_text = "Build your cheap computer"

    print("\nTrying original locator...")

    locator = page.get_by_text(
        broken_text,
        exact=True
    )

    if locator.count() > 0:

        print("Original locator worked")
        locator.first.click()

    else:

        print("Original locator failed")

        generic_healer = GenericLocatorHealer(page)

        candidates_locator = page.locator(
            "a, button, input, label, h1, h2, h3, span"
        )

        candidates = []

        for i in range(candidates_locator.count()):

            element = candidates_locator.nth(i)

            try:
                text = element.inner_text().strip()
            except Exception:
                continue

            if text and text not in candidates:
                candidates.append(text)

        if not candidates:

            print("No candidates found")
            browser.close()
            exit()

        ai_healer = SafeAIHealer(
            threshold=0.85
        )

        healed_text = ai_healer.heal(
            broken_text,
            candidates
        )

        if healed_text:

            healed_locator = page.get_by_text(
                healed_text,
                exact=True
            )

            if healed_locator.count() > 0:

                print("Healed locator found on page")

                healed_locator.first.click()

                print("Healed locator clicked successfully")

            else:

                print("AI candidate not found on page")

    page.wait_for_timeout(3000)

    browser.close()