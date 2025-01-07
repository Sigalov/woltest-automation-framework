from playwright.sync_api import sync_playwright

def test_homepage_can_be_opened():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set to True for CI environments
        page = browser.new_page()
        page.goto('https://example.com')
        assert 'Example Domain' in page.title()
        browser.close()
