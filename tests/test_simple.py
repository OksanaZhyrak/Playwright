from playwright.sync_api import Page, expect
from pages.simple_page import SimplePage

def test_simple_exist(page:Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.check_button_exist()

def test_simple_click(page:Page):
    simple_page = SimplePage(page)
    simple_page.open()
    simple_page.click_button()
    simple_page.check_result_text_is('Submitted')

def test_with_slowmoo(slowmoo):
    assert slowmoo == "30000"
