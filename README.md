# BBC News Headline Scraper

A Python script that scrapes the latest headlines from BBC News website.

## Features

- Scrapes current news headlines from BBC News homepage
- Uses multiple selector patterns to handle website changes
- Removes duplicate headlines
- Saves results to a cleanly formatted text file
- Handles network errors gracefully

## Requirements

- Python 3.x
- requests library (`pip install requests`)
- BeautifulSoup4 library (`pip install beautifulsoup4`)

## Installation required packages:
- pip install -r requirements.txt

## Run the script:
- python Web_Scraper_News_Headlines.py

## The script will:
1. Fetch the latest BBC News homepage
2. Extract headlines using multiple selector patterns
3. Save the headlines to news_headlines.txt

## The script tries these HTML selectors in order:
1. a.ssrcss-1mrs5ns-PromoLink (Primary BBC selector)
2. a.gs-c-promo-heading (Older BBC selector)
3. h3.ssrcss-15wd2r3-PromoHeadline (Alternative selector)
4. a[data-testid="internal-link"] (Generic link selector)
5. h2[class*="Headline"] (Generic headline selector)

##Troubleshooting
If you get 0 headlines:

- Check if BBC has changed their website structure
- Inspect the page to find new selectors
- Update the selectors_to_try list with new patterns

