from playwright.async_api import async_playwright
from typing import Optional, Any
import asyncio

# Global variables to store browser instance and related objects
_playwright: Optional[Any] = None
_browser: Optional[Any] = None
_context: Optional[Any] = None
_page: Optional[Any] = None


async def run(url: str, browser_type: str = "chromium") -> bool:
    """
    Start a browser instance and navigate to the specified URL.
    If browser is already running, it will navigate to the new URL.

    Args:
        url: The URL to navigate to
        browser_type: The type of browser to use ("chromium", "firefox", or "webkit")

    Returns:
        bool: True if navigation was successful, False otherwise
    """
    global _playwright, _browser, _context, _page

    # Validate browser type
    if browser_type not in ["chromium", "firefox", "webkit"]:
        print(f"Invalid browser type: {browser_type}. Using chromium instead.")
        browser_type = "chromium"

    # If browser is not initialized, start a new instance
    if _playwright is None:
        _playwright = await async_playwright().start()
        # Launch the specified browser
        browser_launcher = getattr(_playwright, browser_type)
        _browser = await browser_launcher.launch(headless=False)
        _context = await _browser.new_context()
        _page = await _context.new_page()

    try:
        # Navigate to the URL (whether browser is new or existing) with a timeout
        await _page.goto(url, timeout=30000, wait_until="domcontentloaded")
        # Wait for the page to be fully loaded
        await _page.wait_for_load_state("networkidle")
        return True
    except Exception as e:
        print(f"Error navigating to {url}: {str(e)}")
        return False


async def stop() -> None:
    """
    Close the browser instance if it's running.
    """
    global _playwright, _browser, _context, _page

    if _browser is not None:
        await _browser.close()
        _browser = None

    if _playwright is not None:
        await _playwright.stop()
        _playwright = None

    # Reset other globals
    _context = None
    _page = None


if __name__ == "__main__":
    # Example usage
    async def main():
        # Use a more reliable URL for testing
        await run("https://www.ufile.ca/", browser_type="firefox")
        # Wait a bit to see the page
        await asyncio.sleep(5)
        # Clean up
        await stop()

    asyncio.run(main())
