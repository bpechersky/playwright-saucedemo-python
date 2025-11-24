from playwright.sync_api import Page, expect


class CheckoutOverviewPage:
    def __init__(self, page: Page):
        self.page = page
        self.finish_button = page.get_by_role("button", name="Finish")
        self.complete_header = page.locator("[data-test='complete-header']")

    def finish(self):
        self.finish_button.click()

    def assert_order_completed(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")
