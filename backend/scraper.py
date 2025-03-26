from playwright.sync_api import sync_playwright
import json
import os

ZAPIER_URL = "https://zapier.com/templates/workflows"
N8N_URL = "https://n8n.io/workflows/"

def scrape_zapier():
    """Scrapes automation workflows from Zapier using Playwright"""
    workflows = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(ZAPIER_URL, timeout=60000)

        # Give time for JavaScript to load
        page.wait_for_timeout(5000)

        # Debug: Print a small portion of page content
        print("🔍 Page HTML Preview:")
        print(page.content()[:500])

        try:
            page.wait_for_selector("a.TemplateCard_wrapper__GzoyG", timeout=10000)
        except Exception as e:
            print(f"⚠️ Warning: No templates found. Error: {e}")
            browser.close()
            return []

        # Extract workflow cards
        items = page.query_selector_all("a.TemplateCard_wrapper__GzoyG")
        print(f"🔍 Found {len(items)} workflow templates.")

        for item in items:
            title_elem = item.query_selector("div.TemplateCard_titleWrapper__B95rt span")
            desc_elem = item.query_selector("div.TemplateCard_description__3qrxG span")  # Updated selector

            title_text = title_elem.inner_text().strip() if title_elem else "No Title Found"
            desc_text = desc_elem.inner_text().strip() if desc_elem else "No Description Found"

            print(f"📌 Title: {title_text}")  
            print(f"📌 Description: {desc_text}")  

            workflows.append({
                "title": title_text,
                "description": desc_text,
                "platform": "Zapier"
            })


        browser.close()

    if not workflows:
        print("⚠️ No workflows scraped. The HTML structure may have changed.")

    return workflows


def scrape_n8n():
    """Scrapes automation workflows from N8N using Playwright"""
    workflows = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(N8N_URL, timeout=60000)

        # Allow time for JavaScript to load
        page.wait_for_timeout(5000)

        # Debug: Print part of the page content
        print("🔍 Page HTML Preview:")
        print(page.content()[:500])

        try:
            page.wait_for_selector("h3.font-geomanist.text-lg.text-shades-hazy-white", timeout=10000)
        except Exception as e:
            print(f"⚠️ Warning: No workflows found. Error: {e}")
            browser.close()
            return []

        # Extract workflow titles
        titles = page.query_selector_all("h3.font-geomanist.text-lg.text-shades-hazy-white")
        authors = page.query_selector_all("p.font-geomanist.text-caption-large-medium.text-shades-soft-gray")  # Adjust if necessary

        print(f"🔍 Found {len(titles)} workflow templates.")

        for index, title_elem in enumerate(titles):
            title_text = title_elem.inner_text().strip() if title_elem else "No Title Found"
            author_text = authors[index].inner_text().strip() if index < len(authors) else "Unknown Author"

            print(f"📌 Title: {title_text}")  
            print(f"📌 Description: {author_text}")  

            workflows.append({
                "title": title_text,
                "description": author_text,
                "platform": "N8N"
            })

        browser.close()

    if not workflows:
        print("⚠️ No workflows scraped. The HTML structure may have changed.")

    return workflows


def save_workflows():
    """Saves both Zapier and N8N workflows to a JSON file"""
    zapier_data = scrape_zapier()
    n8n_data = scrape_n8n()

    combined_data = zapier_data + n8n_data  # Merge both lists

    backend_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(backend_dir, "workflows.json")

    if combined_data:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(combined_data, f, indent=4)
        print(f"✅ Data scraped and saved to {json_path}")
    else:
        print("⚠️ No data to save.")


if __name__ == "__main__":
    save_workflows()