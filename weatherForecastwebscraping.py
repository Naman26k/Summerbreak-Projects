import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05349000000007&lon=-118.24531999999999#.XpaofsgzbIU')
soup = BeautifulSoup(page.content,'html.parser')

week = soup.find(id='seven-day-forecast-body')
items = week.find_all(class_='tombstone-container')

period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]

weather_stuff= pd.DataFrame(
    {'period':period_names,
     'short_description':short_description,
     'temperature':temperature,
     })
print(weather_stuff)
weather_stuff.to_csv('weather.csv')
