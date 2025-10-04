# bypass_no_bot.py
import asyncio
from playwright.async_api import async_playwright

async def bypass_gplinks(url: str, timeout_ms: int = 10000) -> str:
    """
    Navigate to `url` using Playwright (WebKit) in headless mode and return the resulting page.url
    after waiting a bit. Adjust timeout_ms if GPLinks has longer timers.
    """
    async with async_playwright() as p:
        browser = await p.webkit.launch(headless=True)
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X)"
        )
        page = await context.new_page()
        await page.goto(url, wait_until="networkidle")
        # wait additional time for any JS timers / redirects on GPLinks
        await page.wait_for_timeout(timeout_ms)
        final = page.url
        await context.close()
        await browser.close()
        return final

# Quick local test-run helper (optional)
if __name__ == "__main__":
    import os
    url = os.environ.get("SAMPLE_URL")
    if not url:
        raise RuntimeError("Set SAMPLE_URL env var (or run from test_bypass.py)")
    print("Testing:", url)
    print(asyncio.run(bypass_gplinks(url)))