import os

import requests

API = "https://app.scrapingbee.com/api/v1/"


def fetch_markdown(url, render_js=False, wait_for=None):
    params = {"url": url, "render_js": str(render_js).lower(), "return_page_markdown": "true"}
    if wait_for:
        params["wait_for"] = wait_for
    resp = requests.get(
        API,
        params=params,
        headers={"Authorization": f"Bearer {os.environ['SCRAPINGBEE_API_KEY']}"},
        timeout=150,
    )
    resp.raise_for_status()
    return resp.text, int(resp.headers.get("Spb-cost", 0))


if __name__ == "__main__":
    markdown, credits = fetch_markdown(
        "https://docsify.js.org/#/quickstart", render_js=True, wait_for=".markdown-section > *"
    )
    print(f"{credits} credits, {len(markdown)} characters")
    print(next(line for line in markdown.splitlines() if "docsify-cli" in line))
