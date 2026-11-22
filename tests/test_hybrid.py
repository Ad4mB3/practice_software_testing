from playwright.sync_api import Playwright, Page, expect
from api.user_api import UserAPI
from pages.home_page import HomePage
from pages.checkout_page import CheckoutPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
import re

def test_skip_login(logged_in_page: Page,):
    # This test uses API token to sign you in 

    main_page = HomePage(logged_in_page)
    expect(main_page.uzivatelske_menu).to_contain_text("Jane Doe")
    print ("Test sucesfully signed you in ")


def test_ading_item_to_cart (logged_in_page: Page,):
    # this log you in with api token, then adds item into cart and checks if its in the cart 

    item_page = HomePage(logged_in_page)
    item_page.product_buying()
    product_page = ProductPage(logged_in_page)
    product_page.adding_to_cart()
    expect(logged_in_page).to_have_url(re.compile(".*checkout.*"))
    cart_page = CheckoutPage(logged_in_page)
    expect(cart_page.quantity_check()).to_have_value("1")


def test_flow_signin_signout(logged_in_page: Page,):
    # sign in after that sign out
    
    page = logged_in_page
    signout_page = HomePage(page)
    signout_page.signout()
    expect(signout_page.signout_check()).to_be_visible() 
    assert page.evaluate("window.localStorage.getItem('auth-token')") is None


def test_complete_checkout_flow(logged_in_page: Page):
    page = logged_in_page
    item_page = HomePage(page)
    item_page.product_buying()
    product_page = ProductPage(page)
    product_page.adding_to_cart()

    cart_page = CheckoutPage(page)
    cart_page.checkout()
    cart_page.fill_billing_address(
        country_code="DE",
        postal_code="60311",
        house_number="654",
        state="Hessen"
    )
    cart_page.payment("cash-on-delivery")

    expect(cart_page.order_confirmation).to_contain_text("Thanks for your order!")


def test_cart_logic(logged_in_page: Page):
    page = logged_in_page
    home_page = HomePage(page)
    product_page = ProductPage(page)
    checkout_page = CheckoutPage(page)

# this block adds two items to the cart 
    home_page.select_first_product()
    product_page.adding_to_cart()
    home_page.go_home()
    home_page.select_second_product()
    product_page.adding_to_cart()
    home_page.go_cart()

    checkout_page.first_item_delete()
    checkout_page.rewriting_quantity()
    expect(checkout_page.quantity).to_have_value("2")

    # this block checks out the items
    checkout_page.checkout()
    checkout_page.fill_billing_address(
            country_code="DE",
            postal_code="60311",
            house_number="654",
            state="Hessen"
        )
    checkout_page.payment("cash-on-delivery")


def test_api_payment_confirmation(logged_in_page: Page):
    page = logged_in_page
    user_api = UserAPI(page.request)

    item_page = HomePage(page)
    item_page.product_buying()
    product_page = ProductPage(page)
    product_page.adding_to_cart()
    cart_page = CheckoutPage(page)
    cart_page.checkout()
    cart_page.fill_billing_address(
        country_code="DE",
        postal_code="60311",
        house_number="654",
        state="Hessen"
    )
    cart_page.payment("cash-on-delivery")

    invoice_number = cart_page.get_invoice_number()
    token = page.evaluate("localStorage.getItem('auth-token')")
    invoices = user_api.get_invoices(token) 
    invoice_numbers = [inv["invoice_number"] for inv in invoices]
    assert invoice_number in invoice_numbers 





    

    














    


