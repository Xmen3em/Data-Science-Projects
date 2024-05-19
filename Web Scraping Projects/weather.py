import pandas as pd
import requests
from bs4 import BeautifulSoup

url = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168')

page = BeautifulSoup(url.content, 'html.parser')
# print(page.prettify())

period_names = []
temp = []
short_desc = []
desc = []

data = page.find('div', {'id': 'seven-day-forecast-container'})
days = data.find_all('div', {'class': 'tombstone-container'})
print(days[0].find('img', {'class': 'forecast-icon'}).attrs['title'])

for i in range(len(days)):
    period_names.append(days[i].find('p', {'class': 'period-name'}).text)
    temp.append(days[i].find('p', {'class': 'temp'}).text)
    short_desc.append(days[i].find('p', {'class': 'short-desc'}).text)
    desc.append(days[i].find('img', {'class': 'forecast-icon'}).attrs['title'])

weather = pd.DataFrame({'desc': desc,
                        'Period': period_names,
                        'short_desc': short_desc,
                        'temp': temp})

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(weather)