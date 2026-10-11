from playwright.sync_api import Page
	#Login function
def login_function(page: Page, username: str, password: str):
	page.locator("#user-name").fill(username)
	page.locator("#password").fill(password)
	page.locator("#login-button").click() 