from playwright.sync_api import Page
from helpers import login_function
from playwright.sync_api import expect

#Leaving everything blank
def test_failed_checkout_fitst_name(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with correct credentials
	login_function(page, "standard_user","secret_sauce")

	#Adding an item to the cart
	page.locator("#add-to-cart-sauce-labs-backpack").click()
	page.locator(".shopping_cart_link").click()

	#Proceeding to checkout
	page.locator("#checkout").click()

	#Proceeding to the next step without filling up the empty fields
	page.locator("#continue").click()

	#Checking if the test was successful
	expect(page.get_by_text("Error: First Name is required")).to_be_visible()
#Putting in only the First name
def test_failed_checkout_last_name(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with correct credentials
	login_function(page, "standard_user","secret_sauce")

	#Adding an item to the cart
	page.locator("#add-to-cart-sauce-labs-backpack").click()
	page.locator(".shopping_cart_link").click()

	#Proceeding to checkout
	page.locator("#checkout").click()

	#Putting in the First name
	page.locator("#first-name").fill("John")

	#Proceeding to the next step
	page.locator("#continue").click()

	#Checking if the test was successful
	expect(page.get_by_text("Error: Last Name is required")).to_be_visible()

#Leaving Postal/Zip code field blank
def test_failed_checkout_postal_code(page: Page):
	page.goto("https://www.saucedemo.com/")

	#Login with correct credentials
	login_function(page, "standard_user","secret_sauce")

	#Adding an item to the cart
	page.locator("#add-to-cart-sauce-labs-backpack").click()
	page.locator(".shopping_cart_link").click()

	#Proceeding to checkout
	page.locator("#checkout").click()

	#Putting in First name and Last name
	page.locator("#first-name").fill("John")
	page.locator("#last-name").fill("Doe")

	#Proceeding to the next step
	page.locator("#continue").click()

	#Checking if the test was successful
	expect(page.get_by_text("Error: Postal Code is required")).to_be_visible()