from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.cart = page.locator("#navbarSupportedContent > ul > li:nth-child(5) > a")
        self.accountbtn = page.locator("#menu")
        self.sign_out_btn = page.locator('[data-test="nav-sign-out"]')
        self.sign_in_btn = page.locator('[data-test="nav-sign-in"]')
        self.home_link = page.locator('[data-test="nav-home"]') 

    

    def go_to(self, url: str):
        self.page.goto(url)
        self.page.wait_for_load_state("networkidle")


    def signout(self):
        self.accountbtn.click()
        self.sign_out_btn.click()

    def signout_check(self):
        return self.sign_in_btn

    def go_home(self):
        self.home_link.click() 

    def go_cart(self):
        self.cart.click()




