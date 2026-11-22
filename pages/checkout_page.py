from playwright.sync_api import expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.quantity = page.locator('[data-test="product-quantity"]')
        self.checkoutbtn = page.get_by_role("button", name="Proceed to checkout")

        # delete buttons 
        self.first_item_deletebtn = page.locator("tbody tr").first.locator("a.btn-danger")
        self.second_item_delete = page.locator("tbody tr").nth(1).locator("a.btn-danger")

        # billing address locators 
        self.country_select = page.locator('[data-test="country"]')
        self.postal_code_input = page.locator('[data-test="postal_code"]')
        self.house_number_input = page.locator('[data-test="house_number"]')
        self.state_input = page.locator('[data-test="state"]')
        self.proceed_step3_btn = page.locator('[data-test="proceed-3"]')

        #payment locators
        self.payment_method = page.locator('[data-test="payment-method"]')
        self.confirm_btn = page.locator('[data-test="finish"]')
        self.success_message = page.locator('[data-test="payment-success-message"]')

        # order confirmation
        self.order_confirmation = page.locator("#order-confirmation")
       

    def quantity_check(self):
        return self.quantity

    def checkout(self):
        self.checkoutbtn.click()
        self.checkoutbtn.click()

    def fill_billing_address(self, country_code: str, postal_code: str, house_number: str, state: str):
        self.country_select.select_option(country_code)
        self.postal_code_input.fill(postal_code)
        self.house_number_input.fill(house_number)
        self.state_input.fill(state)
        self.checkoutbtn.click()
    
    
    def payment(self, method: str):
        self.payment_method.select_option(method)
        self.confirm_btn.click()
        expect(self.success_message).to_be_visible()
        self.confirm_btn.click(delay=200)
        expect(self.order_confirmation).to_be_visible()


    def first_item_delete(self):
        self.first_item_deletebtn.click()
        expect(self.page.locator("tbody tr")).to_have_count(1)

    def rewriting_quantity(self):
        self.quantity.fill("2")

    def get_invoice_number(self) -> str:
        text = self.order_confirmation.inner_text()
        return text.split("is ")[-1].strip().rstrip(".")