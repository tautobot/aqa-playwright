from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_login(self):
        self.page.goto("/login")

    def log_in(self, username: str, password: str):
        self.page.fill("#username", username)
        self.page.fill("#password", password)
        self.page.click("#login-button")
