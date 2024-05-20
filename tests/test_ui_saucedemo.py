import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.page_objects.login_page import LoginPage
from utils.page_objects.inventory_page import InventoryPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

def test_add_item_to_cart(driver):
    test_login(driver)  # Ensure user is logged in
    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()
    assert inventory_page.cart_item_count() == '1'
