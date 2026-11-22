from playwright.sync_api import Playwright
import pytest 

class UserAPI:
    def __init__(self, api_context):
        self.api = api_context
        self.base_url = "https://api.practicesoftwaretesting.com"

    def token_creation(self, email, password):
        api_response = self.api.post(
            f"{self.base_url}/users/login",
            headers={
                "Accept": "application/json"
            },

            data={
                "email": email,
                "password": password,
            },
    )
        assert api_response.status == 200,(
            f"Api failed to get a token {api_response.json()}"
        )
        Token = api_response.json()["access_token"]
        print (f"Here is your token {Token}")

        return Token 

    def get_invoices(self, token: str):
        api_response = self.api.get(
            f"{self.base_url}/invoices",
            headers={
                "Authorization": f"Bearer {token}",
            } 
        )
        assert api_response.status == 200
        return api_response.json()["data"]

    
    