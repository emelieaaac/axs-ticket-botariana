from playwright.sync_api import sync_playwright

URL = "https://www.axs.com/events/1141607/ariana-grande-extra-date-added-tickets"

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(URL, wait_until="networkidle")
        content = page.content().lower()

        signals = [
            "choose from the map",
            "pick your tickets",
            "buy tickets",
            "select seats",
            "find tickets"
        ]

        if any(s in content for s in signals):
            print("🚨 TICKETS MOGELIJK")
        else:
            print("no tickets")

        browser.close()

run()
