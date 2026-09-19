from playwright.sync_api import Page, expect

from page.login_page import LoginPage
from page.dashboard_page import DashboardPage
from page.admin_page import AdminPage
from page.pim_page import PimPage
from page.leave_page import LeavePage
from page.time_page import TimePage


def test_orangehrm(page: Page):

    # Open OrangeHRM
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login",
        timeout=60000
    )

    # Login Page
    login_page = LoginPage(page)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    page.wait_for_load_state("domcontentloaded")

    print("Current URL:", page.url)

    # Dashboard Page
    dashboard_page = DashboardPage(page)

    dashboard_page.verify_dashboard()

    # Admin Page
    dashboard_page.click_admin()

    admin_page = AdminPage(page)

    expect(page).to_have_url(
        "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
    )

    admin_page.enter_username("Admin")
    admin_page.click_search()

    # Go back to Dashboard
    dashboard_page.click_dashboard()
    dashboard_page.verify_dashboard()

    # PIM Page
    dashboard_page.click_pim()

    pim_page = PimPage(page)

    pim_page.verify_pim_page()
    pim_page.click_add()

    pim_page.enter_employee_name(
        "Mohammad",
        "Adnan",
        "Khan"
    )

    pim_page.click_save()

    # Go back to Dashboard
    dashboard_page.click_dashboard()
    dashboard_page.verify_dashboard()

    # Leave Page
    dashboard_page.click_leave()

    leave_page = LeavePage(page)

    leave_page.verify_leave_page()

    # Go back to Dashboard
    dashboard_page.click_dashboard()
    dashboard_page.verify_dashboard()

    # Time Page
    dashboard_page.click_time()

    time_page = TimePage(page)

    time_page.verify_time_page()