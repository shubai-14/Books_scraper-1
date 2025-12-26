# 📚 Books to Scrape – Python Web Scraper

A simple Python web scraper that collects book data from **books.toscrape.com** using `requests` and `BeautifulSoup`.

This project was built as a learning exercise to understand:

* HTML parsing
* pagination handling
* data extraction
* saving scraped data to CSV

---

## 🚀 Features

* Scrapes **all pages automatically**
* Extracts:

  * Book title
  * Price
  * Stock availability
  * Rating (converted to numbers)
  * Image URL
  * Book page URL
* Saves data to a CSV file
* Beginner-friendly and easy to modify

---

## 🧰 Tech Stack

* Python 3
* requests
* beautifulsoup4
* csv

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

Install dependencies:

```bash
pip install requests beautifulsoup4
```

---

## ▶️ Usage

Run the script:

```bash
python scraper.py
```

After running, a file called `books.csv` will be created containing all scraped data.

---

## 📁 Output Example

| Title | Price | Stock | Rating | Image URL | Book URL |
| ----- | ----- | ----- | ------ | --------- | -------- |

---

## 🧠 What I Learned

* How pagination works on websites
* How to use `urljoin` correctly
* How to extract structured data from HTML
* How to organize scraped data
* How to save results into CSV

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
Data is scraped from a public demo website intended for scraping practice.

---

## 📌 Future Improvements

* Add error handling
* Use `requests.Session()` for better performance
* Export to JSON
* Convert into a FastAPI endpoint
* Add logging
* Add CLI arguments

---

## ⭐ Author

Made by **shubai-14**
Learning Python, web scraping, and working toward AI engineering 🚀
