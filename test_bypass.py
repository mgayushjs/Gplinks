# test_bypass.py
import asyncio
import os
from bypass_no_bot import bypass_gplinks

async def main():
    url = os.environ.get("SAMPLE_URL")
    if not url:
        raise RuntimeError("SAMPLE_URL environment variable is required (set in GitHub Secrets).")

    print("Starting bypass test for:", url)
    try:
        final = await bypass_gplinks(url, timeout_ms=12000)
        print("✅ Final URL:", final)
    except Exception as e:
        print("❌ Bypass failed with exception:", repr(e))
        raise

if __name__ == "__main__":
    asyncio.run(main())