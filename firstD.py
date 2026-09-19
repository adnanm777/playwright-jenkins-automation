from playwright.sync_api import Page, expect


def test_open_demo_webshop(page: Page):
    page.goto("https://demowebshop.tricentis.com/")

    logo = page.get_by_alt_text("Wrong Logo")

    expect(logo).to_be_visible()

    products = page.locator('h2 > a[href*="computer"]')

    product_count = products.count()

    print(f"Number of products found: {product_count}")

    print("Product names:")
    for i in range(product_count):
        product_name = products.nth(i).inner_text()
        print(f"- {product_name}")

    print("Test case executed successfully")
    print(page.title())

    page.wait_for_timeout(3000)
