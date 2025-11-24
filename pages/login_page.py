from playwright.sync_api import Page, expect
from .inventory_page import InventoryPage


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def login(self, username: str, password: str) -> InventoryPage:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return InventoryPage(self.page)

    def login_expect_failure(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        expect(self.error_message).to_be_visible()

    def assert_on_page(self):
        expect(self.login_button).to_be_visible()
