import requests
from bs4 import BeautifulSoup

# URL of the news website to scrape
URL = 'https://www.bbc.com/news'

# Headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

try:
    # Send GET request
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Try multiple selectors to find headlines (BBC changes these frequently)
    selectors_to_try = [
        'a.ssrcss-1mrs5ns-PromoLink',  # New BBC selector
        'a.gs-c-promo-heading',         # Older BBC selector
        'h3.ssrcss-15wd2r3-PromoHeadline',  # Alternative new selector
        'a[data-testid="internal-link"]',    # Another possible selector
        'h2[class*="Headline"]'              # Generic headline selector
    ]
    
    cleaned_headlines = []
    
    # for selector in selectors_to_try:
    selector = selectors_to_try[4]  # Use the second selector for simplicity
    headlines = soup.select(selector)
    if headlines:
        for h in headlines:
            text = h.get_text().strip()
            if text and len(text.split()) > 3:  # Only keep meaningful headlines
                cleaned_headlines.append(text)
        # break  # Stop after first successful selector
    
    # If still no headlines, try a more aggressive approach
    if not cleaned_headlines:
        potential_headlines = soup.find_all(['h1', 'h2', 'h3', 'h4', 'a'])
        for h in potential_headlines:
            text = h.get_text().strip()
            if (len(text.split()) > 3 and 
                not any(word in text.lower() for word in ['menu', 'account', 'sign in', 'more'])):
                cleaned_headlines.append(text)
    
    # Remove duplicates while preserving order
    seen = set()
    cleaned_headlines = [h for h in cleaned_headlines if not (h in seen or seen.add(h))]
    
    # Save to a text file
    if cleaned_headlines:
        with open('news_headlines.txt', 'w', encoding='utf-8') as file:
            for i, headline in enumerate(cleaned_headlines[:50], 1):  # Limit to top 50
                file.write(f"{i}. {headline}\n")
        
        print(f"Successfully saved {len(cleaned_headlines)} headlines to news_headlines.txt")
    else:
        print("Warning: No headlines found. The website structure may have changed.")
        print("Try inspecting the page to find new selectors.")

except requests.exceptions.RequestException as e:
    print(f"Network error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
