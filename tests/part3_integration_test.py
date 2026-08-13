import requests
from playwright.sync_api import sync_playwright, expect

API_BASE = "https://api.workflowpro.com"
TOKEN = "demo-bearer-token"
TENANT = "company1"

def create_project_api(name="Case Study Project by Vivek"):
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "X-Tenant-ID": TENANT,
        "Content-Type": "application/json"
    }
    payload = {
        "name": name,
        "description": "Created during Bynry case study",
        "team_members": ["admin@company1.com"]
    }
    response = requests.post(f"{API_BASE}/api/v1/projects", json=payload, headers=headers)
    assert response.status_code in [200, 201]
    return response.json().get("id")


def test_project_creation_flow():
    project_name = "Case Study Project by Vivek"
    project_id = create_project_api(project_name)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login as Company 1
        page.goto("https://app.workflowpro.com/login", wait_until="networkidle")
        page.fill("#email", "admin@company1.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        page.wait_for_url("**/dashboard", timeout=15000)

        page.wait_for_selector(".project-card", timeout=10000)
        expect(page.locator(f"text={project_name}")).to_be_visible()

        # Tenant Isolation Check
        page.goto("https://app.workflowpro.com/login", wait_until="networkidle")
        page.fill("#email", "user@company2.com")
        page.fill("#password", "password123")
        page.click("#login-btn")
        page.wait_for_url("**/dashboard", timeout=15000)

        expect(page.locator(f"text={project_name}")).to_have_count(0)

        browser.close()
