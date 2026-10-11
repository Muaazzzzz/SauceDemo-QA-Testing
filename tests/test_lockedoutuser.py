from playwright.sync_api import Page, expect
from helpers import login_function

def test_locked_out_user(page :Page):
	page.goto("https://www.saucedemo.com/")

	#Login in with the locked out user credentials
	login_function(page, "locked_out_user",  "secret_sauce")

	#Checking if the test was successful
	expect(page.get_by_text("Epic sadface: Sorry, this user has been locked out.")).to_be_visible()