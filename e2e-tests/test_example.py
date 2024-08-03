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

def test_click_button(browser):
    page = browser.new_page()
    page.goto("http://localhost:3000")
    assert page.title() == "Create Next App"
    
    click_me_button = page.query_selector('[data-testid="click-me"]')
    click_me_button.click()
    
    greetings_element = page.query_selector('[data-testid="greetings"]')
    assert greetings_element.inner_text() == "Hello World"

def test_click_modal_and_close(browser):
    page = browser.new_page()
    page.goto("http://localhost:3000")
    assert page.title() == "Create Next App"
    
    click_me_button = page.query_selector('[data-testid="click-me"]')
    click_me_button.click()
    
    greetings_element = page.query_selector('[data-testid="greetings"]')
    assert greetings_element.inner_text() == "Hello World"

    close_button = page.query_selector('[data-testid="close-modal"]')
    close_button.click()

    click_me = page.query_selector('[data-testid="click-me"]')
    assert click_me.inner_text() == "Click Me"

def test_click_modal_enter_text_and_close(browser):
    page = browser.new_page()
    page.goto("http://localhost:3000")
    assert page.title() == "Create Next App"
    
    click_me_button = page.query_selector('[data-testid="click-me"]')
    click_me_button.click()
    
    greetings_element = page.query_selector('[data-testid="greetings"]')
    assert greetings_element.inner_text() == "Hello World"

    input_text = page.query_selector('[data-testid="entry-box"]')
    input_text.fill("Welcome to Playwright")

    close_button = page.query_selector('[data-testid="close-modal"]')
    close_button.click()

    message = page.query_selector('[data-testid="message"]')
    assert message.inner_text() == "Welcome to Playwright"