from playwright.sync_api import Page
from helpers import login_function
from playwright.sync_api import expect

def test_removing_items_from_the_cart(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with correct credentials
	login_function(page, "standard_user","secret_sauce" )

	#Adding an item to the cart
	page.locator("#add-to-cart-sauce-labs-backpack").click()
	page.locator(".shopping_cart_link").click()

	#Removing an item from the cart
	page.locator("#remove-sauce-labs-backpack").click()

	#Checking if the test is successful
	expect(page.get_by_text("Sauce Labs Backpack")).to_be_hidden()