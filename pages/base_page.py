# pages/base_page.py
class BasePage:
    def __init__(self, page):
        self.page = page

    def go_to(self, url):
        self.page.goto(url)

    def is_element_visible(self, selector):
        return self.page.is_visible(selector)

    def set_viewport_size(self, width=1920, height=1080):
        """Set the viewport to a wider size"""
        self.page.set_viewport_size({"width": width, "height": height})
