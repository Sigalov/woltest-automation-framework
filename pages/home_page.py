# pages/home_page.py
import allure
from pages.base_page import BasePage
from utils.logger import setup_logger

logger = setup_logger()

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = 'https://wolt.com/en/discovery'
        
        # Header Locators
        self._wolt_logo = '[data-test-id="HeaderWoltLogoLink"]'
        self._address_select_button = '[data-test-id="header.address-select-button"]'
        self._address_text = '[data-test-id="header.address-select-button.address-text"]'
        self._search_input = '[data-test-id="SearchInput"]'
        self._clear_search_button = '[data-test-id="ClearSearchButton"]'
        self._login_button = '[data-test-id="UserStatus.Login"]'
        self._signup_button = '[data-test-id="UserStatus.Signup"]'
        
        # Navigation Locators
        self._product_line_nav = '[data-test-id="ProductLineNavigation"]'
        self._product_line = '[data-test-id="ProductLine"]'
        self._product_line_image = '[data-test-id="ProductLine.Image"]'
        self._product_line_title = '[data-test-id="ProductLine.Title"]'
        
        # Discovery Content Locators
        self._main_content = '[data-test-id="MainDiscoveryContent"]'
        self._see_all_link = '[data-test-id="Discovery.AllLink"]'

    @allure.step("Click on Wolt logo")
    def click_logo(self):
        logger.info("Clicking on Wolt logo")
        self.page.click(self._wolt_logo)
        
    @allure.step("Open address selection dialog")
    def open_address_selection(self):
        logger.info("Opening address selection dialog")
        self.page.click(self._address_select_button)
        
    @allure.step("Get current address")
    def get_current_address(self):
        logger.info("Getting current address text")
        return self.page.text_content(self._address_text)
        
    @allure.step("Search for {query}")
    def search(self, query):
        logger.info(f"Searching for: {query}")
        search_box = self.page.locator(self._search_input)
        search_box.fill(query)
        search_box.press('Enter')
        
    @allure.step("Clear search")
    def clear_search(self):
        logger.info("Clearing search input")
        clear_button = self.page.locator(self._clear_search_button)
        if clear_button.is_visible():
            clear_button.click()
            
    @allure.step("Click login button")
    def click_login(self):
        logger.info("Clicking login button")
        self.page.click(self._login_button)
        
    @allure.step("Click signup button")
    def click_signup(self):
        logger.info("Clicking signup button")
        self.page.click(self._signup_button)
        
    @allure.step("Get all product categories")
    def get_product_categories(self):
        logger.info("Getting all product categories")
        categories = []
        product_lines = self.page.locator(self._product_line).all()
        for line in product_lines:
            title = line.locator(self._product_line_title)
            categories.append(title.text_content())
        return categories
        
    @allure.step("Navigate to category {category_name}")
    def navigate_to_category(self, category_name):
        logger.info(f"Navigating to category: {category_name}")
        product_lines = self.page.locator(self._product_line).all()
        for line in product_lines:
            title = line.locator(self._product_line_title)
            if category_name in title.text_content():
                line.click()
                return
        # Fallback to exact text match if not found in product lines
        self.page.get_by_text(category_name, exact=True).click()
        
    @allure.step("Click 'See all' for section {section_name}")
    def click_see_all(self, section_name):
        logger.info(f"Clicking 'See all' for section: {section_name}")
        see_all_links = self.page.locator(self._see_all_link).all()
        for link in see_all_links:
            if section_name.lower() in link.get_attribute('aria-label').lower():
                link.click()
                break

    @allure.step("Navigate to homepage")
    def navigate_home(self):
        """Navigate to the homepage"""
        logger.info(f"Navigating to {self.url}")
        self.set_viewport_size()  # Set wider viewport before navigation
        self.page.goto(self.url)
        self.page.wait_for_load_state("networkidle")
        
    @allure.step("Check if navigation is visible")
    def is_navigation_visible(self):
        logger.info("Checking if navigation is visible")
        return self.page.locator(self._product_line_nav).is_visible(timeout=15000)
        
    @allure.step("Navigate to restaurants section")
    def go_to_restaurants(self):
        logger.info("Navigating to restaurants section")
        self.navigate_to_category("Restaurants")
        
    @allure.step("Navigate to stores section")
    def go_to_stores(self):
        logger.info("Navigating to stores section")
        self.navigate_to_category("Stores")
        
    @allure.step("Search for {query}")
    def search_for(self, query):
        logger.info(f"Searching for: {query}")
        self.search(query)

    @allure.step("Navigate to {section_name}")
    def navigate_to(self, section_name):
        logger.info(f"Navigating to: {section_name}")
        self.page.get_by_text(section_name, exact=True).click()

    def navigate(self):
        """Navigate to the homepage"""
        self.page.goto("https://wolt.com/en/discovery")
