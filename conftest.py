from playwright.sync_api import sync_playwright, Page
import pytest

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page: Page = context.new_page()
        page.set_viewport_size({'height': 1080, 'width': 1920})
        yield page
        browser.close()
