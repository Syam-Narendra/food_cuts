import json
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth
from cookies import cookies


def open_instagram():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--disable-features=IsolateOrigins,site-per-process",
            ],
        )
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        context.add_cookies(cookies)
        page = context.new_page()
        page.goto("https://www.instagram.com/reels/DHYngWzTNld", wait_until="load")
        page.wait_for_timeout(5000)
        print("Scrolling started... Press CTRL+C to stop.")
        last_url = page.url
        data = []
        jsonFilePath = "reelsLinksData.json"
        while True:
            page.keyboard.press("PageDown")
            time.sleep(2)
            new_url = page.url
            if new_url != last_url:
                print("New Reel URL:", new_url)
                with open(jsonFilePath, "r") as file:
                    try:
                        oldFileData = json.load(file)
                        data = oldFileData
                    except:
                        data = []
                with open(jsonFilePath, "w") as file:
                    newUrl = {"link": new_url}
                    data.append(newUrl)
                    json.dump(data, file, indent=4)
                last_url = new_url


open_instagram()
