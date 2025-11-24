from playwright.sync_api import Page
from .checkout_overview_page import CheckoutOverviewPage


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")

    def fill_customer_info_and_continue(self, first_name: str, last_name: str, postal_code: str) -> CheckoutOverviewPage:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()
        return CheckoutOverviewPage(self.page)
