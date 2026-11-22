import pytest 
from api.user_api import UserAPI
from playwright.sync_api import Playwright, Page


@pytest.fixture
def api_token_cretion(playwright: Playwright):
    api_context= playwright.request.new_context()
    login_api = UserAPI(api_context)
    token = login_api.token_creation("customer@practicesoftwaretesting.com", "welcome01")

    yield token 

    api_context.dispose()

@pytest.fixture 
def logged_in_page(page: Page, playwright: Playwright):
    api_context= playwright.request.new_context()
    login_api = UserAPI(api_context)
    token = login_api.token_creation("customer@practicesoftwaretesting.com", "welcome01")
    page.goto("https://practicesoftwaretesting.com/")
    page.wait_for_load_state("networkidle")
    page.evaluate(f"window.localStorage.setItem('auth-token', '{token}')")
    page.reload()
    page.wait_for_load_state("networkidle")

    yield page
    api_context.dispose()
    
