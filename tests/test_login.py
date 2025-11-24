from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


VALID_USER = "standard_user"
VALID_PASSWORD = "secret_sauce"


def test_successful_login(login_page: LoginPage):
    inventory_page = login_page.login(VALID_USER, VALID_PASSWORD)
    inventory_page.assert_logged_in()


def test_invalid_login_shows_error(login_page: LoginPage):
    login_page.login_expect_failure("locked_out_user", "wrong_password")
