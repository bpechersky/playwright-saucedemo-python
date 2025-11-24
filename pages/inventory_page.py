from playwright.sync_api import Page, expect
from .cart_page import CartPage


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_container = page.locator("[data-test='inventory-container']")
        self.cart_icon = page.locator("#shopping_cart_container")

    def assert_logged_in(self):
        expect(self.inventory_container).to_be_visible()

    def add_item_to_cart_by_name(self, product_name: str):
        item = self.page.get_by_text(product_name).locator("xpath=ancestor::div[@class='inventory_item']")
        add_button = item.get_by_role("button", name="Add to cart")
        add_button.click()

    def open_cart(self) -> CartPage:
        self.cart_icon.click()
        return CartPage(self.page)
