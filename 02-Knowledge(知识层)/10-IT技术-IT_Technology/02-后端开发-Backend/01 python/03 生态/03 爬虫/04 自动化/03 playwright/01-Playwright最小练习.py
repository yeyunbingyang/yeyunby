"""Playwright 最小练习：访问页面、定位标题并保存截图。"""

from pathlib import Path

from playwright.sync_api import expect, sync_playwright


TARGET_URL = "https://example.com"
SCREENSHOT_DIR = Path(__file__).parent / "screenshots"
SCREENSHOT_PATH = SCREENSHOT_DIR / "example-domain.png"


def main() -> None:
    """运行一次最小的 Chromium 自动化流程。"""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 720})
            response = page.goto(
                TARGET_URL,
                wait_until="domcontentloaded",
                timeout=30_000,
            )
            if response is not None and not response.ok:
                raise RuntimeError(
                    f"页面访问失败：{response.status} {response.status_text}"
                )

            heading = page.get_by_role("heading", name="Example Domain")
            expect(heading).to_be_visible(timeout=10_000)

            page.screenshot(path=SCREENSHOT_PATH, full_page=True)
            print(f"页面标题：{page.title()}")
            print(f"截图路径：{SCREENSHOT_PATH}")
        finally:
            browser.close()


if __name__ == "__main__":
    main()
