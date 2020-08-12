#! /usr/bin/env python3
# get_open_weather.py - Prints the weather for a location from the commmand line.

appid = "**************"  # Create an account at https://openweathermap.org/api/ to obtain an API key

import json
import requests
import sys


def kelvin_convert(kelvin):
    fahrenheit = (kelvin - 273.15) * 9 / 5 + 32
    return fahrenheit


# Compute location from command line arguments.
if len(sys.argv) < 2:
    print("Usage: get_open_weather.py city_name, state code, 2-letter_country_code")
    sys.exit()
location = ",".join(sys.argv[1:])


# TODO: Download the JSON data from OpenWeatherMap.org's API.
url = f"https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={appid}"
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
# print(response.text)

# TODO: Load JSON data into a python variable.
weather_data = json.loads(response.text)

# Print weather descriptions
w = weather_data["list"]
todays_temp = kelvin_convert(w[0]["main"]["temp"])
feels_like = kelvin_convert(w[0]["main"]["feels_like"])
humidity = w[0]["main"]["humidity"]
print(f"Current weather in {location}")
print(
    f"Today's temp: {round(float(todays_temp),2)} - Feels like: {round(float(feels_like),2)} - Humidity: {humidity}%"
)
print(w[0]["weather"][0]["main"], "-", w[0]["weather"][0]["description"])
print()
print("Tomorrow:")
print(w[1]["weather"][0]["main"], "-", w[1]["weather"][0]["description"])
print()
print("Day after tomorrow:")
print(w[2]["weather"][0]["main"], "-", w[2]["weather"][0]["description"])
