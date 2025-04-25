from income_tax_agent import playwright_helper


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


async def get_t5_info(name: str) -> str | list[dict]:
    """
    Select a specific T5 slip by its name and extract all input fields information.

    This function navigates to the specified T5 slip and extracts information from all
    input fields found on the page, including their titles, box numbers, and values.

    Args:
        name: The name of the T5 slip to select (e.g., "T5: BBC")

    Returns:
        str | list[dict]: Either an error message as a string if the operation fails,
                         or a list of dictionaries with each containing:
                         - 'title': The label of the input field
                         - 'box': The box number (if available)
                         - 'value': The current value in the input field (if any)
    """
    page = playwright_helper._page
    if page is None:
        return "Ufile didn't load, please try again"

    # Use a more specific selector that targets only the div elements containing "T5:" text
    # This targets the exact elements containing T5 labels
    t5_elements = page.locator('div.tocLabel').filter(has_text='T5:')
    all_t5s = await t5_elements.all()

    t5_found = False
    for t5 in all_t5s:
        if name in await t5.inner_text():
            await t5.click()
            t5_found = True
            break

    if not t5_found:
        return f"T5 slip with name '{name}' not found."

    # Give the page a moment to load the T5 content
    await page.wait_for_timeout(1000)

    # Find all fieldsets that contain input fields (similar to the test.html structure)
    fieldsets = page.locator('fieldset')
    count = await fieldsets.count()

    # Create a new list to store the formatted field data
    formatted_fields = []

    # Process each fieldset individually
    for i in range(count):
        fieldset = fieldsets.nth(i)
        item = {}

        # Try to find the title/label
        title_element = fieldset.locator('.int-label').first
        title = await title_element.inner_text() if await title_element.count() > 0 else ""

        # Try to find the box number
        box_element = fieldset.locator('.boxNumberContent').first
        box = await box_element.inner_text() if await box_element.count() > 0 else ""

        # Try to find the input value
        input_element = fieldset.locator('input[type="text"]').first
        value = await input_element.input_value() if await input_element.count() > 0 else ""

        # Only add the field if we found a title
        if title:
            item['title'] = title.strip()
            item['box'] = box.strip() if box else None
            item['value'] = value.strip() if value else None

            formatted_fields.append(item)

    return formatted_fields


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
            result = await get_t5_info("T5: BBC")
            print(result)

    asyncio.run(main())
