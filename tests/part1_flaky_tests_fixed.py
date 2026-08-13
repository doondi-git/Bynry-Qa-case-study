import pytest
from playwright.sync_api import sync_playwright, expect

def test_user_login_fixed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1280, "height": 720})
        page = context.new_page()

        page.goto("https://app.workflowpro.com/login", wait_until="networkidle")
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        page.wait_for_url("**/dashboard", timeout=15000)
        welcome = page.locator(".welcome-message")
        expect(welcome).to_be_visible(timeout=10000)

        context.close()
        browser.close()


def test_multi_tenant_access_fixed():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://app.workflowpro.com/login", wait_until="networkidle")
        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")

        page.wait_for_selector(".project-card", state="visible", timeout=15000)
        projects = page.locator(".project-card").all()

        for project in projects:
            text = project.inner_text()
            assert "Company2" in text

        browser.close()
