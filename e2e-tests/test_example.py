import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_example(browser):
    page = browser.new_page()
    page.goto("http://localhost:3000")
    assert page.title() == "Create Next App"