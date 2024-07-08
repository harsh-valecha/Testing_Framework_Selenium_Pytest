import pytest
from utils.config import Config
from pages.login_page import LoginPage

def test_login(driver):
    driver.get(Config.BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.enter_username('testuser')
    login_page.enter_password('password')
    login_page.click_login()

    assert "Dashboard" in driver.title
