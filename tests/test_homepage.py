import allure
import pytest
from pages.home_page import HomePage

@allure.feature("Wolt Homepage")
class TestHomepage:
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Setup fixture that runs before each test"""
        self.home_page = HomePage(page)
        self.home_page.navigate()
        yield
    
    @allure.story("Basic Navigation")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_homepage_loads(self):
        """Verify homepage loads with correct URL and navigation"""
        assert "wolt.com/en/discovery" in self.home_page.page.url
        assert "TLV - Herzliya area" in self.home_page.get_current_address()

    @allure.story("Navigation Menu")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_navigation_to_restaurants(self):
        """Verify navigation to restaurants section"""
        self.home_page.go_to_restaurants()
        assert "restaurants" in self.home_page.page.url.lower()

    @allure.story("Navigation Menu")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    def test_navigation_to_stores(self):
        """Verify navigation to stores section"""
        self.home_page.go_to_stores()
        assert "stores" in self.home_page.page.url.lower()

    @allure.story("Search Functionality")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_functionality(self):
        """Verify search functionality"""
        search_term = "burger"
        self.home_page.search_for(search_term)
        assert search_term.lower() in self.home_page.page.url.lower()
        assert self.home_page.is_search_results_visible()
        self.home_page.clear_search()

    @allure.story("Product Categories")
    @allure.severity(allure.severity_level.NORMAL)
    def test_product_categories(self):
        """Verify product categories are displayed correctly"""
        categories = self.home_page.get_product_categories()
        assert "Restaurants" in categories
        assert "Other Stores" in categories

    @allure.story("Section Navigation")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize("section", [
        "Lunch near you",
        "0 ₪ delivery fee",
        "Popular right now"
    ])
    def test_section_navigation(self, section):
        """Verify navigation to different sections"""
        self.home_page.click_see_all(section)
        # Add specific assertions for each section

    @allure.story("Authentication")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_button(self):
        """Verify login button functionality"""
        self.home_page.click_login()
        assert self.home_page.is_login_modal_visible() 