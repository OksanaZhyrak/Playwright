from asyncio import get_event_loop

from playwright.async_api import Page, expect, async_playwright
import asyncio
import pytest
import re

from pytest_playwright.pytest_playwright import browser


# @pytest.fixture(scope="session")
# def event_loop():
#     policy = asyncio.get_event_loop_policy()
#     loop = policy.new_event_loop()
#     yield loop
#     loop.close()

@pytest.mark.asyncio
async def test_first():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.google.com/')
        await expect(page).to_have_title('Google')
        mail_link = page.get_by_role('link', name='Gmail')
        # print(mail_link.get_attribute('href'))
        await expect(mail_link).to_have_attribute('href', re.compile('https://mail.google.com/mail/&ogbl'))
        # input_field = page.locator('#APjFqb')
        input_field = page.locator('xpath=//*[@id="APjFqb"]')
        await input_field.fill('cat')
        search_button = page.locator('(//input[@name="btnK"])[2]')
        await search_button.click()
        await expect(page).to_have_title(re.compile('cat', re.IGNORECASE))

@pytest.mark.asyncio
async def test_dynamic_props():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://demoqa.com/dynamic-properties')
        button = page.locator('#visibleAfter')
        await button.click()
        await page.screenshot(type='jpeg', path='shot.jpg')

@pytest.mark.asyncio
async def test_iframe():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
        toggler = page.frames[1].locator('css=.navbar-toggler-icon')
        await toggler.click()
        await page.screenshot(type='jpeg', path='toggler.jpg')

@pytest.mark.asyncio
async def test_drag():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
        await page.drag_and_drop('#rect-draggable', '#rect-droppable')
        await page.screenshot(type='jpeg', path='drag.jpg')

@pytest.mark.asyncio
async def test_select():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://www.qa-practice.com/elements/button/disabled')
        await page.locator('#id_select_state').select_option('enabled')
        await page.screenshot(type='jpeg', path='select.jpg')

@pytest.mark.asyncio
async def test_hover():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto('https://magento.softwaretestingboard.com/')
        await page.locator('#ui-id-4').hover()
        await page.locator('#ui-id-9').hover()
        await page.screenshot(type='jpeg', path='hover.jpg')

