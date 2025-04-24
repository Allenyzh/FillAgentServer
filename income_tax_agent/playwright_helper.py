from playwright.sync_api import sync_playwright
from typing import Optional, Any
import logging


logger = logging.getLogger(__name__)

# Global variables to store browser instance and related objects
_playwright: Optional[Any] = None
_browser: Optional[Any] = None
_context: Optional[Any] = None
_page: Optional[Any] = None


def run(url: str, browser_type: str = "chromium") -> bool:
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
        logger.warning(
            f"Invalid browser type: {browser_type}. Using chromium instead.")
        browser_type = "chromium"

    # Check if browser is still alive if it was initialized
    if _browser is not None:
        try:
            # Additional check to see if the browser has been manually closed
            if not _browser.is_connected():
                logger.warning(
                    "Browser or context appears to be closed manually")
                raise Exception("Browser context is no longer valid")
        except Exception as e:
            logger.warning(f"Browser instance appears to be dead: {str(e)}")
            # Clean up the dead browser references
            _browser = None
            _context = None
            _page = None
            _playwright = None

    # If browser is not initialized, start a new instance
    if _playwright is None:
        logger.info(f"Initializing new {browser_type} browser instance")
        _playwright = sync_playwright().start()
        # Launch the specified browser
        browser_launcher = getattr(_playwright, browser_type)
        _browser = browser_launcher.launch(headless=False)
        _context = _browser.new_context()
        _page = _context.new_page()
    else:
        logger.debug("Using existing browser instance")

    try:
        # Extra check before navigation to ensure page is still valid
        if _page is None or not hasattr(_page, "goto"):
            logger.warning("Page object is invalid, creating a new page")
            # If context is still valid, try to create a new page
            try:
                _page = _context.new_page()
            except Exception:
                # If context is not valid, rebuild everything
                logger.warning("Context is invalid, restarting browser")
                _browser.close() if _browser else None
                _playwright.stop() if _playwright else None
                _playwright = sync_playwright().start()
                browser_launcher = getattr(_playwright, browser_type)
                _browser = browser_launcher.launch(headless=False)
                _context = _browser.new_context()
                _page = _context.new_page()

        # Navigate to the URL (whether browser is new or existing) with a timeout
        logger.info(f"Navigating to {url}")
        _page.goto(url, timeout=30000, wait_until="domcontentloaded")
        # Wait for the page to be fully loaded
        _page.wait_for_load_state("networkidle")
        logger.info(f"Successfully loaded {url}")
        return True
    except Exception as e:
        logger.error(f"Error navigating to {url}: {str(e)}")
        # If we get a thread-related error, clean up and restart on next run
        if "thread" in str(e).lower() and "exited" in str(e).lower():
            logger.warning(
                "Browser thread has exited, will restart on next run")
            stop()  # This will clean up all resources
        return False


def stop() -> None:
    """
    Close the browser instance if it's running.
    """
    global _playwright, _browser, _context, _page

    if _browser is not None:
        logger.info("Closing browser")
        _browser.close()
        _browser = None

    if _playwright is not None:
        logger.info("Stopping playwright")
        _playwright.stop()
        _playwright = None

    # Reset other globals
    _context = None
    _page = None
    logger.debug("Browser resources cleaned up")


def run_browser_tool(url: str) -> bool:
    """
    Start a browser instance and navigate to the specified URL.

    Args:
        url: The URL to navigate to

    Returns:
        bool: True if navigation was successful, False otherwise
    """
    return run(url)


def stop_browser_tool() -> None:
    """
    Close the browser instance if it's running.
    """
    logger.info("Stopping browser tool")
    stop()


if __name__ == "__main__":
    # Example usage
    run_browser_tool("https://www.ufile.ca/")
    # To add a delay if needed, you can use time.sleep instead of asyncio.sleep
    import time
    time.sleep(10)

    run_browser_tool("https://www.ufile.ca/")
    # stop_browser_tool()
