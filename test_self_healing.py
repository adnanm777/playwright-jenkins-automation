from pathlib import Path
from playwright.sync_api import Page
from healing.safe_ai_healer import SafeAIHealer
import logging


logging.basicConfig(
    filename="self_healing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def test_self_healing(page: Page):

    screenshot_dir = Path("screenshots")
    screenshot_dir.mkdir(exist_ok=True)

    logging.info("Self-healing test started")

    page.goto(
        "https://demowebshop.tricentis.com/",
        wait_until="domcontentloaded",
        timeout=60000
    )

    broken_text = "Build your cheap computer"

    print("\nTrying original locator...")

    logging.info(
        f"Trying original locator: {broken_text}"
    )

    locator = page.get_by_text(
        broken_text,
        exact=True
    )

    if locator.count() > 0:

        print("Original locator worked")

        logging.info(
            "Original locator worked"
        )

        locator.first.click()

    else:

        print("Original locator failed")

        logging.warning(
            "Original locator failed"
        )

        page.screenshot(
            path=str(
                screenshot_dir / "locator_failure.png"
            ),
            full_page=True
        )

        print("Failure screenshot saved")

        logging.info(
            "Failure screenshot saved"
        )

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

        logging.info(
            f"DOM candidates collected: {len(candidates)}"
        )

        if not candidates:

            logging.error(
                "No DOM candidates found"
            )

            raise Exception(
                "No DOM candidates found"
            )

        print("\nCalling AI healer...")

        logging.info(
            "Calling AI healer"
        )

        ai_healer = SafeAIHealer(
            threshold=0.85
        )

        print("AI healer created")

        healed_text = ai_healer.heal(
            broken_text,
            candidates
        )

        print("AI healer response received")

        logging.info(
            f"AI selected candidate: {healed_text}"
        )

        if healed_text:

            healed_locator = page.get_by_text(
                healed_text,
                exact=True
            )

            if healed_locator.count() > 0:

                print("Healed locator found on page")

                logging.info(
                    "Healed locator found on page"
                )

                healed_locator.first.click()

                print(
                    "Healed locator clicked successfully"
                )

                logging.info(
                    "Healed locator clicked successfully"
                )

            else:

                page.screenshot(
                    path=str(
                        screenshot_dir /
                        "healed_locator_failure.png"
                    ),
                    full_page=True
                )

                logging.error(
                    "AI candidate not found on page"
                )

                raise Exception(
                    "AI candidate not found on page"
                )

        else:

            page.screenshot(
                path=str(
                    screenshot_dir /
                    "ai_healing_rejected.png"
                ),
                full_page=True
            )

            logging.error(
                "AI healing rejected"
            )

            raise Exception(
                "AI healing rejected"
            )

    logging.info(
        "Self-healing test completed successfully"
    )