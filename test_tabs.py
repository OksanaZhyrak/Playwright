from playwright.sync_api import Page
from pages.new_tab_example_page import NewTabExamplePage


def test_tabs(page: Page):
    nomads = NewTabExamplePage(page)
    nomads.open()
    context = page.context  # Отримуємо контекст з поточної сторінки
    nomads.open_in_new_tab(context)  # Відкриваємо нову вкладку і отримуємо її




