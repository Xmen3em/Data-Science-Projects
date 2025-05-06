# Job Scraper

This project scrapes job postings from Indeed.com and saves them to a CSV file for use in AI applications.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the scraper:
   ```bash
   python scraper.py
   ```
3. The scraped data will be saved in `jobs.csv`.

## Customization
- Change the `BASE_URL` in `scraper.py` to search for different roles or locations.
- Extend the code to parse more fields as needed.

**Note:** Always respect the website's robots.txt and terms of service. This code is for educational purposes.
