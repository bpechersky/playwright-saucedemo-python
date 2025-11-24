import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    page.goto(base_url)
    return LoginPage(page)
