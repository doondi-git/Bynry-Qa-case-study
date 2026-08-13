from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-btn")

    def navigate(self):
        self.page.goto("https://app.workflowpro.com/login", wait_until="networkidle")

    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_btn.click()
        self.page.wait_for_url("**/dashboard", timeout=15000)
