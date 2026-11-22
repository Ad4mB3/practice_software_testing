from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        available_products = page.locator("a.card").filter(has_not_text="Out of stock")
        self.first_product = page.locator('.card').first
        self.second_product = page.locator("a.card").nth(1) 
        self.uzivatelske_menu = page.locator('[data-test="nav-menu"]')
        

    def select_first_product(self):
        self.first_product.click()

    def select_second_product(self):
        self.second_product.click()

    def product_buying(self):
        self.select_first_product()




    


    