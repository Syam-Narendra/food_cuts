import asyncio
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext
from playwright.async_api import Error as PlaywrightError
from cookies import cookies
import time
async def request_handler(context: PlaywrightCrawlingContext) -> None:
    try:
        context.log.info(f"Processing URL: {context.request.url}")
        print(cookies)
        await context.page.context.add_cookies(cookies)
        initial_url = context.page.url
        await context.push_data({"link": initial_url})
        context.log.info(f"Initial Reel URL: {initial_url}")

        # Press "PageDown" to move to the next reel
        time.sleep(5000)
        await context.page.keyboard.press("PageDown")
        print("PageDown pressed")
        time.sleep(10000)  # import time

        # Wait for the URL to change

        # Capture the new URL
        new_url = context.page.url
        await context.push_data({"link": new_url})
        context.log.info(f"New Reel URL: {new_url}")

    except PlaywrightError as e:
        context.log.error(f"Playwright error on {context.request.url}: {e}")
    except Exception as e:
        context.log.error(f"Unexpected error on {context.request.url}: {e}")

async def main():
    crawler = PlaywrightCrawler(headless=False)
    crawler.router.default_handler(request_handler)

    try:
        await crawler.run(["https://www.instagram.com/reels/DA8WnYvyrl9/"])
    except Exception as e:
        print(f"Failed to run crawler: {e}")

if __name__ == "__main__":
    asyncio.run(main())
