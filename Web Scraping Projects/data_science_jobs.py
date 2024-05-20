import pandas as pd
import requests
from bs4 import BeautifulSoup

total_jobs = 1027

job_name = []
company_name = []
Location = []
date = []
skills = []
Responsibilities = []
links = []

i = 0
while True:
    page = requests.get(f'https://wuzzuf.net/search/jobs/?q=data%20science&start={i}')
    soup = BeautifulSoup(page.content, 'html.parser')

    i += 1
    page_num = int(total_jobs) // 15
    if i > page_num:
        print('terminate')
        break


    big_div = soup.find_all('div', {'class': 'css-1gatmva e1v1l3u10'})
    for items in range(len(big_div)):
        job_name.append(big_div[items].h2.find('a', {'class': 'css-o171kl'}).text)
        name_location_date = big_div[items].find('div', {'class': 'css-d7j1kk'})
        company_name.append(name_location_date.find('a', {'class': 'css-17s97q8'}).text.strip())
        Location.append(name_location_date.find('span', {'class': 'css-5wys0k'}).text.strip())

        new = big_div[items].find('div', {'class': 'css-do6t5g'})
        old = big_div[items].find('div', {'class': 'css-4c4ojb'})
        if new is None:
            date.append(old.text.strip())
        else:
            date.append(new.text.strip())

        links.append(big_div[items].h2.find('a', {'class': 'css-o171kl'}).attrs['href'])

    # print(i)

for link in links:
    pages = requests.get(link)
    soup = BeautifulSoup(pages.content, 'html.parser')

    skill = soup.find_all('a', {'class': 'css-g65o95'})
    s = ''

    for a in range(len(skill)):
        a_skill = skill[a].find('span', {'class': 'css-6to1q'})
        a_skill = a_skill.find('span', {'class': 'css-158icaa'}).text
        s += a_skill+" "

    skills.append(s)

data = pd.DataFrame({
    'Job_name': job_name,
    'Company_name': company_name,
    'Location': Location,
    'Date': date
    'skills': skills
})

print(data.sample())
data.to_csv('Data Scintist Jops.csv',index=False)