#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import sys

def fetch_website(url):
    try:
        # Send GET request
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text content
        text = soup.get_text()
        
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        print(f"Successfully fetched content from: {url}\n")
        print("=" * 80)
        print(text)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        sys.exit(1)

if __name__ == "__main__":
    url = "https://docs.anthropic.com/en/docs/claude-code/common-tasks"
    fetch_website(url)