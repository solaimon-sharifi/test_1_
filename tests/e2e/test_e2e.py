"""End-to-end tests using Playwright to exercise the HTML UI."""
import time
import requests
import pytest
from playwright.sync_api import sync_playwright


def test_homepage_add(tmp_path):
    # CI will start a server on port 8001 before running this test. If the
    # server isn't running locally, skip the E2E test to avoid a hard failure.
    url = "http://127.0.0.1:8001/"
    try:
        requests.get(url, timeout=0.5)
    except Exception:
        pytest.skip("E2E server not running on 127.0.0.1:8001")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        # set inputs
        page.fill('#left', '7')
        page.fill('#right', '3')
        page.click('#add')
        # small wait for fetch to complete
        time.sleep(0.2)
        text = page.inner_text('#result')
        assert 'Result:' in text
        assert '10' in text
        browser.close()
