import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional


def scrape_website_links(url: str) -> Optional[List[str]]:
    """
    Fetches the content of a URL and extracts all the 'href' attributes
    from 'a' (anchor) tags using Beautiful Soup.

    Args:
        url: The URL of the website to scrape.

    Returns:
        A list of link URLs (strings) found on the page, or None if the
        request failed.
    """
    print(f"--- 🚀 Starting to scrape: {url} ---")

    # 1. Fetch the HTML content
    try:
        # Use a common user-agent header to avoid being blocked by some sites
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        html_content = response.text

    except requests.exceptions.RequestException as e:
        print(f"--- ❌ Error fetching the URL: {e} ---")
        return None

    # 2. Parse the HTML content
    #
    soup = BeautifulSoup(html_content, 'html.parser')

    # 3. Find and extract data

    # Find all 'a' tags (links) in the document
    all_links = soup.find_all('a')

    extracted_links: List[str] = []

    print(f"--- ✅ Found {len(all_links)} anchor tags ---")

    # Iterate over the found tags and extract the 'href' attribute
    for link in all_links:
        href = link.get('href')
        if href:
            extracted_links.append(href)

    return extracted_links


# --- Main execution ---
if __name__ == "__main__":
    # NOTE: Replace this with the actual URL you want to scrape.
    # For this example, we'll use a widely accessible, generic-content page.
    target_url = "https://www.amazon.com"

    links = scrape_website_links(target_url)

    if links:
        print("\n--- 🔗 Extracted Links (First 10) ---")

        for i, link in enumerate(links[:10]):
            print(f"[{i + 1}] {link}")

        if len(links) > 10:
            print(f"...and {len(links) - 10} more links.")
    else:
        print("\n--- ⚠️ No links were extracted or an error occurred. ---")