from playwright.sync_api import sync_playwright, expect, Page
import re
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


def test_first(page):
    page.goto('https://www.google.com/')
    expect(page).to_have_title('Google')
    mail_link = page.get_by_role('link', name='Gmail')
    #print(mail_link.get_attribute('href'))
    expect(mail_link).to_have_attribute('href', re.compile('https://mail.google.com/mail/&ogbl'))
    #input_field = page.locator('#APjFqb')
    input_field = page.locator('xpath=//*[@id="APjFqb"]')
    input_field.fill('cat')
    search_button = page.locator('(//input[@name="btnK"])[2]')
    search_button.click()
    expect(page).to_have_title(re.compile('cat', re.IGNORECASE))

