# conftest.py
import pytest
import allure
from playwright.sync_api import sync_playwright
from utils.logger import setup_logger

# Setup logger
logger = setup_logger()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        logger.info("Starting browser session")
        browser = p.chromium.launch(
            headless=False,
            args=['--start-maximized', '--disable-gpu'],
            channel="chrome"  # Use stable Chrome instead of Chromium
        )
        yield browser
        logger.info("Closing browser session")
        browser.close()

@pytest.fixture
def page(browser):
    logger.info("Creating new page")
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1980},
        ignore_https_errors=True
    )
    page = context.new_page()
    yield page
    logger.info("Closing page")
    page.close()
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call":
        if report.failed:
            logger.error(f"Test failed: {item.name}")
            try:
                if "page" in item.funcargs:
                    allure.attach(
                        item.funcargs["page"].screenshot(),
                        name="screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                logger.error(f"Failed to capture screenshot: {e}")
