from playwright.sync_api import Page, expect
from .checkout_page import CheckoutPage


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.get_by_role("button", name="Checkout")

    def assert_item_in_cart(self, product_name: str):
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def checkout(self) -> CheckoutPage:
        self.checkout_button.click()
        return CheckoutPage(self.page)
