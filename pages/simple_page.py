from playwright.sync_api import expect
import time

BUTTON = '#submit-id-submit'
RESULT = '#result-text'

class SimplePage:

    def __init__(self, page, slowmoo=None):
        self.page = page
        self.slowmoo = int(slowmoo) / 1000 if slowmoo is not None else 0

    def open(self):
        self.page.goto('https://www.qa-practice.com/elements/button/simple')
        time.sleep(self.slowmoo)

    def check_button_exist(self):
        button = self.page.locator(BUTTON)
        time.sleep(self.slowmoo)  # Додаємо паузу перед перевіркою
        expect(button).to_be_visible()

    def click_button(self):
        button =self.page.locator(BUTTON)
        time.sleep(self.slowmoo)
        button.click()

    def check_result_text_is(self, text):
        result = self.page.locator(RESULT)
        time.sleep(self.slowmoo)
        expect(result).to_have_text(text)