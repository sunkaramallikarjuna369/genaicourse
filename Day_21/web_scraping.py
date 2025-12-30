"""Day 21: Web Scraping with Python
Learn to scrape web pages using BeautifulSoup and requests.
"""

import requests
from bs4 import BeautifulSoup
import csv
from typing import List, Dict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class WebScraper:
    """Web scraper for extracting data from websites."""
    
    def __init__(self, timeout=10):
        self.timeout = timeout
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def fetch_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a web page."""
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_links(self, soup: BeautifulSoup, url: str) -> List[str]:
        """Extract all links from a page."""
        if not soup:
            return []
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('http'):
                links.append(href)
        return links
    
    def extract_text(self, soup: BeautifulSoup, selector: str) -> List[str]:
        """Extract text using CSS selector."""
        if not soup:
            return []
        elements = soup.select(selector)
        return [elem.get_text(strip=True) for elem in elements]
    
    def extract_table(self, soup: BeautifulSoup, table_index=0) -> List[Dict]:
        """Extract table data from HTML."""
        if not soup:
            return []
        tables = soup.find_all('table')
        if table_index >= len(tables):
            return []
        
        table = tables[table_index]
        headers = [th.get_text(strip=True) for th in table.find_all('th')]
        rows = []
        
        for tr in table.find_all('tr')[1:]:
            cells = [td.get_text(strip=True) for td in tr.find_all('td')]
            if cells:
                rows.append(dict(zip(headers, cells)))
        
        return rows
    
    def save_to_csv(self, data: List[Dict], filename: str):
        """Save scraped data to CSV file."""
        if not data:
            logger.warning("No data to save")
            return
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            logger.info(f"Data saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")

# Example usage
if __name__ == "__main__":
    scraper = WebScraper()
    
    # Scrape example
    url = "https://example.com"
    soup = scraper.fetch_page(url)
    
    if soup:
        links = scraper.extract_links(soup, url)
        print(f"Found {len(links)} links")
        
        # Extract headings
        headings = scraper.extract_text(soup, "h1")
        print(f"Headings: {headings}")
        
        # Extract tables
        tables = scraper.extract_table(soup)
        print(f"Tables extracted: {tables}")
