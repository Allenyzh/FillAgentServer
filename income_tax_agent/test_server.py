import asyncio
from playwright.async_api import async_playwright
import sys


async def main():
    custom_port = 3000

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[f'--remote-debugging-port={custom_port}']
        )
        print(f"Playwright instance address: http://localhost:{custom_port}")

        # Create a page
        page = await browser.new_page()

        # Use a never-resolving future to keep the script running indefinitely
        # This is more reliable than using wait_for_timeout
        await asyncio.Future()

        # Alternative: use a very long but finite timeout (not recommended)
        # await page.wait_for_timeout(2147483647)  # Maximum 32-bit integer

asyncio.run(main())
