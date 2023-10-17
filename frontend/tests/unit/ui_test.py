from selene import by, have
from selene.support.shared.jquery_style import s
from selene.support.shared import browser

browser.config.driver_name = 'chrome'
browser.config.base_url = 'http://localhost:8080/'
browser.config.timeout = 10
browser.open('')


def test_has_seven_blocks():
    s(by.xpath("//div[contains(text(), 'Enter your')]")).should(have.text("Enter your name:"))