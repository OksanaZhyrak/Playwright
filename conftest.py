from playwright.sync_api import sync_playwright, Page
import pytest

def pytest_addoption(parser):
    parser.addoption("--slowmoo", action="store", default=None, help="Set slowmoo value")

@pytest.fixture()
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page: Page = context.new_page()
        page.set_viewport_size({'height': 1080, 'width': 1920})
        yield page
        browser.close()
@pytest.fixture()
def slowmoo(request):
    return request.config.getoption("--slowmoo")