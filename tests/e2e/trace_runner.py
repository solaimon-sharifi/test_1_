"""Run a small Playwright scenario and save a trace + screenshot for CI artifacts.

This script is intended to be invoked by CI after the test server is running.
It will produce files under the `artifacts/` directory:
 - artifacts/trace.zip
 - artifacts/screenshot.png

If the server is not reachable the script exits with code 2.
"""
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright
import requests


ARTIFACT_DIR = Path(os.environ.get("ARTIFACT_DIR", "artifacts"))
ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)

URL = os.environ.get("E2E_URL", "http://127.0.0.1:8001/")


def main():
    # Ensure server is up
    try:
        requests.get(URL, timeout=1.0)
    except Exception as exc:
        print(f"Server not reachable at {URL}: {exc}")
        sys.exit(2)

    trace_path = ARTIFACT_DIR / "trace.zip"
    screenshot_path = ARTIFACT_DIR / "screenshot.png"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        # start tracing
        context.tracing.start(screenshots=True, snapshots=True)
        page = context.new_page()
        page.goto(URL)
        page.fill('#left', '7')
        page.fill('#right', '3')
        page.click('#add')
        time.sleep(0.2)
        page.screenshot(path=str(screenshot_path))
        # stop tracing and save
        context.tracing.stop(path=str(trace_path))
        browser.close()

    print(f"Wrote artifacts: {trace_path} and {screenshot_path}")


if __name__ == "__main__":
    main()
