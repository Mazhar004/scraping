# Data scraper solution using Scrapy Framework

## Installation

### Python Version

- Python == 3.6

### Library Installation

#### Linux

- Virtual Environment
  - `python -m venv venv`
  - `source venv/bin/activate`
- Library Install
  - `pip install --upgrade pip`
  - `pip install --upgrade setuptools`
  - `pip install -r requirements.txt`

## Projects

- **Amazon**
  - Amazon best sellers books data collections [Link](/amazon)
  - `cd amazon`
  - `scrapy crawl amazon_books -o books.json`
- **ToScrape**
  - Basics of scrapy on **toscrape** website [Link](/quotetutorial)
  - `cd quotetutorial`
  - `scrapy crawl quotes -o quotes.json`