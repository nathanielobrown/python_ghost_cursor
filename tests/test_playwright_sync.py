from playwright.sync_api import sync_playwright
from python_ghost_cursor.playwright_sync import create_cursor


def test_create_cursor():
    with sync_playwright() as p:
        selector = "h1"
        browser = p.chromium.launch(channel="chrome", headless=False)
        page = browser.new_page()
        cursor = create_cursor(page)
        page.goto("https://www.example.com")
        page.wait_for_selector(selector)
        cursor.click(selector)
