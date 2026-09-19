
from playwright.sync_api import Page, expect
from healing.failure_analyzer import FailureAnalyzer
from healing.locator_healer import LocatorHealer


def test_open_demo_webshop(page: Page):

    page.goto("https://demowebshop.tricentis.com/")

    # Intentionally broken locator
    broken_alt = "Tricentis Demo Shop"

    logo = page.get_by_alt_text(broken_alt)

    try:

        expect(logo).to_be_visible()

        print("Original locator worked!")

    except AssertionError as e:

        print("\n❌ Original locator failed")

        # Collect failure evidence
        analyzer = FailureAnalyzer(page)

        evidence = analyzer.collect_page_evidence(
            str(e)
        )

        print("\n========== FAILURE EVIDENCE ==========")

        print("URL:")
        print(evidence["url"])

        print("\nTITLE:")
        print(evidence["title"])

        print("\nERROR:")
        print(evidence["error"])

        print("\n=======================================")

        # Start self-healing
        print("\n🔧 Starting locator healing...")

        healer = LocatorHealer(page)

        healed_alt, score = healer.heal_alt_text(
            broken_alt
        )

        print("\n========== HEALING RESULT ==========")

        print("Broken locator:")
        print(broken_alt)

        print("\nHealed locator:")
        print(healed_alt)

        print("\nConfidence:")
        print(round(score, 2))

        print("\n====================================")

        # Retry using healed locator
        if healed_alt:

            healed_logo = page.get_by_alt_text(
                healed_alt
            )

            expect(
                healed_logo
            ).to_be_visible()

            print(
                "\n✅ SELF-HEALING SUCCESSFUL!"
            )

        else:

            print(
                "\n❌ SELF-HEALING FAILED"
            )

            raise e
