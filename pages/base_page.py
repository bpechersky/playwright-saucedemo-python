from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def expect_url_contains(self, text: str):
        expect(self.page).to_have_url(lambda u: text in u)
