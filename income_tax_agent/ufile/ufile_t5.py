import playwright_helper


async def get_all_t5() -> list | str:
    """
    Get all T5 slips from the current member.

    Returns:
        list: A list containing only the T5 slip information
    """
    page = playwright_helper._page
    if page is None:
        return "Ufile didn't load, please try again"

    # Use a more specific selector that targets only the div elements containing "T5:" text
    # This targets the exact elements containing T5 labels
    t5_elements = page.locator('div.tocLabel').filter(has_text='T5:')
    all_t5s = await t5_elements.all()

    t5_values = []
    for t5 in all_t5s:
        t5_values.append(await t5.inner_text())

    return t5_values

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

            members = await get_all_t5()
            print(members)

    asyncio.run(main())
