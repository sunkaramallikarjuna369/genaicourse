#!/usr/bin/env python3
"""
Day 7: Web Scraping with Beautiful Soup
Learning how to extract data from websites
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin
import csv
import time

# 1. Basic Web Scraping
def basic_scraping():
    """Basic web scraping example"""
    url = "https://example.com"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Parse the HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.title.string if soup.title else "No title found"
        print(f"Page title: {title}")
        
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

# 2. Extract Specific Elements
def extract_elements(soup):
    """Extract specific HTML elements"""
    if not soup:
        return
    
    # Find all paragraphs
    paragraphs = soup.find_all('p')
    print(f"Found {len(paragraphs)} paragraphs")
    
    # Find all links
    links = soup.find_all('a')
    print(f"\nFound {len(links)} links:")
    for link in links[:5]:  # Print first 5 links
        href = link.get('href')
        text = link.get_text()
        print(f"  {text}: {href}")
    
    return paragraphs, links

# 3. Extract Data from Tables
def extract_table_data(url):
    """Extract data from HTML tables"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find tables
        tables = soup.find_all('table')
        print(f"Found {len(tables)} tables")
        
        # Extract data from first table
        if tables:
            table = tables[0]
            rows = []
            
            for tr in table.find_all('tr'):
                cols = [td.get_text(strip=True) for td in tr.find_all(['td', 'th'])]
                rows.append(cols)
            
            return rows
    except Exception as e:
        print(f"Error: {e}")
    
    return None

# 4. Web Scraping with CSS Selectors
def scrape_with_selectors(url):
    """Use CSS selectors to extract data"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Select specific elements using CSS selectors
        # Example: select all div with class 'article'
        articles = soup.select('div.article')
        print(f"Found {len(articles)} articles")
        
        # Select elements with specific ID
        header = soup.select_one('div#header')
        if header:
            print(f"Header text: {header.get_text(strip=True)[:100]}")
        
        return articles
    except Exception as e:
        print(f"Error: {e}")
    
    return None

# 5. Extract News Articles
def scrape_news(url):
    """Scrape news articles from a website"""
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = []
        
        # Find article containers
        for item in soup.find_all('article')[:5]:
            # Extract headline
            headline = item.find('h2')
            headline_text = headline.get_text(strip=True) if headline else "No headline"
            
            # Extract description
            description = item.find('p')
            description_text = description.get_text(strip=True) if description else "No description"
            
            # Extract link
            link = item.find('a')
            link_url = link.get('href') if link else "No link"
            
            articles.append({
                'headline': headline_text,
                'description': description_text,
                'url': link_url
            })
        
        return articles
    except Exception as e:
        print(f"Error scraping news: {e}")
        return []

# 6. Save Scraped Data to CSV
def save_to_csv(data, filename='scraped_data.csv'):
    """Save scraped data to CSV file"""
    if not data:
        print("No data to save")
        return
    
    try:
        # If data is list of dictionaries
        if isinstance(data[0], dict):
            df = pd.DataFrame(data)
            df.to_csv(filename, index=False)
            print(f"Data saved to {filename}")
        # If data is list of lists
        else:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerows(data)
            print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data: {e}")

# 7. Respect Robots.txt and Rate Limiting
def polite_scraping(base_url):
    """Practice polite web scraping"""
    # Check robots.txt
    try:
        robots_url = urljoin(base_url, '/robots.txt')
        print(f"Check {robots_url} before scraping")
    except Exception as e:
        print(f"Error: {e}")
    
    # Add delay between requests
    time.sleep(2)  # Wait 2 seconds
    
    print("Polite scraping: Added delay to be respectful")

if __name__ == "__main__":
    print("=== Day 7: Web Scraping ===")
    
    # Test basic scraping
    # soup = basic_scraping()
    # if soup:
    #     extract_elements(soup)
    
    print("\nWeb scraping examples loaded!")
    print("Remember to:")
    print("- Check website's robots.txt")
    print("- Respect rate limits")
    print("- Use appropriate headers")
    print("- Check terms of service")
    print("- Don't overload servers")
