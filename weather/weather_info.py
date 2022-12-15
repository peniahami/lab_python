#!/usr/bin/env python3

"""Print weather info for specified city

Prompt user for city and look up weather on openweathermap
"""

import requests, json

# Prompt for city name
cityname = input("City : ")

# openweathermap API key
owm_api_key = "9e8aa36520d971ae18f31342aad820f7"

# get json object with city weather info
x = requests.get("http://api.openweathermap.org/data/2.5/weather?appid=" + owm_api_key + "&q=" + cityname).json()

# code = "404" means city could not be found in database
if x["cod"] != "404":
	# print the weather descrption and temperature
	print(" The weather in " + cityname +  " is " +
					str(x["weather"][0]["description"]) +
		"( " + str(x["main"]["temp"]) + "°K )")

else:
	print(" City Not Found ")
