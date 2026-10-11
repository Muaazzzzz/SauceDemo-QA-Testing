from playwright.sync_api import Page
from helpers import login_function
from playwright.sync_api import expect

def test_login_page(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with correct credentials
	login_function(page, "standard_user","secret_sauce" )

	#Checking if the test is successfull
	expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
	print("Login page loaded successfully!")

	#Adding an item to the cart
	page.locator("#add-to-cart-sauce-labs-backpack").click()
	page.locator(".shopping_cart_link").click()

	#Checking if the test is successful
	expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()

def test_invalid_login_page(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with incorrect credentials
	login_function(page, "standard_user", "incorrectpassword")

	#Checking if the test is successful
	expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service")).to_be_visible()


