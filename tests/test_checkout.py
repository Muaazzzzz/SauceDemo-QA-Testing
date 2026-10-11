from playwright.sync_api import Page
from helpers import login_function
from playwright.sync_api import expect

def test_checkout(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with correct credentials
	login_function(page, "standard_user","secret_sauce" )

	#Adding an item to the cart
	page.locator("#add-to-cart-sauce-labs-backpack").click()
	page.locator(".shopping_cart_link").click()

	#Proceeding to checkout
	page.locator("#checkout").click()

	#Filling up the information needed
	page.locator("#first-name").fill("John")
	page.locator("#last-name").fill("Doe")
	page.locator("#postal-code").fill("10000")

	#Proceeding to the next step
	page.locator("#continue").click()

	#Finishing the purchase
	page.locator("#finish").click()

	#Checking if the test was successful
	expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
	expect(page.get_by_role("heading", name="Thank you for your order!")).to_be_visible()