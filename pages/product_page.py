from playwright.sync_api import Page, Playwright
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.add_to_cart = page.get_by_text("Add to cart")


    def adding_to_cart(self):
        self.add_to_cart.click()
        self.cart.click()
        
