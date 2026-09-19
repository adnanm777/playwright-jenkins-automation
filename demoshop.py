from playwright.sync_api import Page, expect
from healing.failure_analyzer import FailureAnalyzer
from healing.locator_healer import LocatorHealer
from healing.generic_locator_healer import GenericLocatorHealer


def test_open_demo_webshop(page: Page):

    page.goto("https://demowebshop.tricentis.com/")

    # ------------------------------------------------
    # 1. BROKEN LOGO LOCATOR
    # ------------------------------------------------

    broken_alt = "Tricentis Demo Shop"

    logo = page.get_by_alt_text(broken_alt)

    try:

        expect(logo).to_be_visible()

        print("\n✅ Original logo locator worked!")

    except AssertionError as e:

        print("\n❌ Original logo locator failed")

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

        print("\n🔧 Starting logo self-healing...")

        healer = LocatorHealer(page)

        healed_alt, score = healer.heal_alt_text(
            broken_alt
        )

        print("\n========== LOGO HEALING RESULT ==========")

        print("Broken locator:")
        print(broken_alt)

        print("\nHealed locator:")
        print(healed_alt)

        print("\nConfidence:")
        print(round(score, 2))

        print("\n==========================================")

        if healed_alt:

            healed_logo = page.get_by_alt_text(
                healed_alt
            )

            expect(
                healed_logo
            ).to_be_visible()

            print(
                "\n✅ LOGO SELF-HEALING SUCCESSFUL!"
            )

        else:

            print(
                "\n❌ LOGO SELF-HEALING FAILED"
            )

            raise e

    # ------------------------------------------------
    # 2. PRODUCT COUNT
    # ------------------------------------------------

    products = page.locator(
        'h2 > a[href*="computer"]'
    )

    product_count = products.count()

    print(
        f"\nNumber of products found: "
        f"{product_count}"
    )

    print("\nProduct names:")

    for i in range(product_count):

        product_name = products.nth(
            i
        ).inner_text()

        print(
            f"- {product_name}"
        )

    # ------------------------------------------------
    # 3. GENERIC LOCATOR HEALING
    # ------------------------------------------------

    print(
        "\n=========================================="
    )

    print(
        "🤖 TESTING GENERIC LOCATOR HEALER"
    )

    print(
        "=========================================="
    )

    generic_healer = GenericLocatorHealer(
        page
    )

    # Intentionally broken product text

    broken_text = "Build your cheap computer"

    print(
        f"\n❌ Broken text locator:"
    )

    print(
        broken_text
    )

    healed_text, score = generic_healer.find_by_text(
        broken_text
    )

    print(
        "\n========== GENERIC HEALING RESULT =========="
    )

    print(
        "Broken text:"
    )

    print(
        broken_text
    )

    print(
        "\nHealed text:"
    )

    print(
        healed_text
    )

    print(
        "\nConfidence:"
    )

    print(
        round(score, 2)
    )

    print(
        "\n============================================="
    )

    if healed_text:

        healed_element = page.get_by_text(
            healed_text,
            exact=True
        )

        expect(
            healed_element.first
        ).to_be_visible()

        print(
            "\n✅ GENERIC LOCATOR SELF-HEALING SUCCESSFUL!"
        )

    else:

        print(
            "\n❌ GENERIC LOCATOR SELF-HEALING FAILED"
        )

        raise AssertionError(
            "Could not heal locator"
        )

        # ------------------------------------------------
    # 4. LOW CONFIDENCE TEST
    # ------------------------------------------------

    print(
        "\n=========================================="
    )

    print(
        "🛡️ TESTING LOW CONFIDENCE HEALING"
    )

    print(
        "=========================================="
    )

    broken_text = "XYZ Random Product 123"

    print(
        "\n❌ Broken text:"
    )

    print(
        broken_text
    )

    healed_text, score = generic_healer.find_by_text(
        broken_text
    )

    print(
        "\n========== LOW CONFIDENCE RESULT =========="
    )

    print(
        "Healed text:"
    )

    print(
        healed_text
    )

    print(
        "\nConfidence:"
    )

    print(
        round(score, 2)
    )

    print(
        "\n============================================"
    )

    if healed_text is None:

        print(
            "\n🛡️ SAFE HEALING:"
        )

        print(
            "❌ Healing rejected because confidence is too low"
        )

    else:

        print(
            "\n⚠️ Unexpected healing occurred"
        )




    print(
        "\nTest case executed successfully"
    )

    print(
        "Page title:",
        page.title()
    )