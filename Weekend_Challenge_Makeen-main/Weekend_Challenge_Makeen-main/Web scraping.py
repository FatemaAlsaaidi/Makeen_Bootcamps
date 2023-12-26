# -*- coding: utf-8 -*-
"""
Created on Sat May 27 10:48:42 2023

@author: HP
"""

import requests
from bs4 import BeautifulSoup
import json

# enter city name
city = input("Enter the name of city:" )

# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content

# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

# formatting data
data = str.split('\n')
time = data[0]
weather_conditions = data[1]

# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
humidity_wind_speed = listdiv[5].text

# getting humidity and wind speed data
humidity = humidity_wind_speed.split(',')[0]
wind_speed = humidity_wind_speed.split(',')[1]

# printing all data
print("Temperature is", temp)
print("Time: ", time)
print("weather conditions: ", weather_conditions)
print("humidity: ", humidity)
print("wind speed: ", wind_speed)

# storing the weather data in JSON file
with open("weather_data.json", "w") as f:
    json.dump({
        "temperature": temp,
        "time": time,
        "weather conditions": weather_conditions,
        "humidity": humidity,
        "wind speed": wind_speed
    }, f, indent=4)
