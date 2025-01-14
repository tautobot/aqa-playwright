import pytest
from pages.login_page import LoginPage

@pytest.mark.e2e
def test_user_can_log_in(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()
    login_page.log_in("user@example.com", "password123")
    assert page.locator("#welcome-message").inner_text() == "Welcome, User!"
