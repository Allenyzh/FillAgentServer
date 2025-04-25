import playwright_helper


async def get_all_members() -> list | str:
    """
    Get all members from the current page.

    Returns:
        list: A dictionary containing the members
    """
    page = playwright_helper._page
    if page is None:
        return "Ufile didn't load, please try again"

    # Get all spans inside the list items, including both appSelected and applicants classes
    # Use 'ul.intApps li' to select all list items within the ul.intApps element
    lis = page.locator('ul.intApps li a span')
    all_lis = await lis.all()

    span_values = []
    for li in all_lis:
        span_values.append(await li.inner_text())

    return span_values


if __name__ == "__main__":
    import asyncio

    from playwright.async_api import async_playwright

    async def main():
        # The correct format for connecting to Chrome DevTools Protocol is:
        # ws://localhost:<port>/devtools/browser/<id>
        # But for Playwright, you can use this simpler format:
        instance_address = 'http://localhost:3000/'

        async with async_playwright() as p:
            playwright_helper._playwright = p
            # Connect to the browser with close_browser=False to keep it open after script exits
            playwright_helper._browser = await p.chromium.connect_over_cdp(
                instance_address
            )

            # Get all browser contexts - contexts is a property, not a method
            contexts = playwright_helper._browser.contexts
            if contexts:
                playwright_helper._context = contexts[0]
                # Get all pages in the first context - pages is a property, not a method
                pages = playwright_helper._context.pages
                if pages:
                    playwright_helper._page = pages[0]
                    print(f"Successfully connected to existing page: {await playwright_helper._page.title()}")
                else:
                    print("No pages found in the context. Creating a new page.")
                    playwright_helper._page = await playwright_helper._context.new_page()
            else:
                print("No contexts found. Creating a new context and page.")
                playwright_helper._context = await playwright_helper._browser.new_context()
                playwright_helper._page = await playwright_helper._context.new_page()

            members = await get_all_members()
            print(members)

    asyncio.run(main())
