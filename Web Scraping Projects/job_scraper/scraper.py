import requests
from bs4 import BeautifulSoup
import csv

# URL of the job site (Indeed example, can be changed)
BASE_URL = "https://www.indeed.com/jobs?q=python+developer&l="

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
}

def fetch_job_listings(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []
    for div in soup.find_all('div', attrs={'class': 'job_seen_beacon'}):
        title = div.find('h2', attrs={'class': 'jobTitle'})
        company = div.find('span', attrs={'class': 'companyName'})
        location = div.find('div', attrs={'class': 'companyLocation'})
        summary = div.find('div', attrs={'class': 'job-snippet'})
        jobs.append({
            'title': title.text.strip() if title else '',
            'company': company.text.strip() if company else '',
            'location': location.text.strip() if location else '',
            'summary': summary.text.strip() if summary else ''
        })
    return jobs
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'company', 'location', 'summary'])
        writer.writeheader()
        for job in jobs:    
            writer.writerow(job)

def main():
    print("Scraping jobs from Indeed...")
    jobs = fetch_job_listings(BASE_URL)
    save_to_csv(jobs, 'jobs.csv')
    print(f"Saved {len(jobs)} jobs to jobs.csv")

if __name__ == "__main__":
    main()
