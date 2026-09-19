from playwright.sync_api import sync_playwright
from healing.generic_locator_healer import GenericLocatorHealer
from healing.ai_healer import AIHealer
import re


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False, slow_mo=500)

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

        print("✅ Original locator worked")

        locator.first.click()

    else:

        print("❌ Original locator failed")

        healer = GenericLocatorHealer(page)

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

            print("❌ No candidates found")

            browser.close()
            exit()

        ai = AIHealer()

        result = ai.find_best_candidate(
            broken_text,
            candidates
        )

        print("\n========== AI RESULT ==========")
        print(result)
        print("===============================")

        best_match = re.search(
            r"BEST:\s*(.+)",
            result
        )

        confidence_match = re.search(
            r"CONFIDENCE:\s*([0-9.]+)",
            result
        )

        if best_match and confidence_match:

            best_candidate = best_match.group(1).strip()
            confidence = float(
                confidence_match.group(1)
            )

            print("\n🛡️ SAFE HEALING:")

            if confidence >= 0.85:

                print("✅ Healing accepted")
                print(
                    f"Using candidate: {best_candidate}"
                )
                print(
                    f"Confidence: {confidence:.2f}"
                )

                healed_locator = page.get_by_text(
                    best_candidate,
                    exact=True
                )

                if healed_locator.count() > 0:

                    print(
                        "✅ Healed locator found on page"
                    )

                    healed_locator.first.click()

                    print(
                        "✅ Healed locator clicked successfully"
                    )

                else:

                    print(
                        "❌ AI candidate not found on page"
                    )

            else:

                print("❌ Healing rejected")
                print(
                    f"Confidence: {confidence:.2f}"
                )

        else:

            print("❌ Could not understand AI response")

    page.wait_for_timeout(3000)

    browser.close()

