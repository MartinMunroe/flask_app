# -*- coding: utf-8 -*-

import forecastio
from geopy.geocoders import Nominatim
import os
from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = environ['WEATHER_API']

# address = input("Type in a location for up to the moment weather: ")

# print (location)

def get_lat1(the_string):
	geolocator = Nominatim()
	location = geolocator.geocode(the_string)
	return (location.latitude)

def get_long1(another_string):
	geolocator = Nominatim()
	location = geolocator.geocode(another_string)
	return (location.longitude)

# geo_lat = get_lat1(location)
# geo_long = get_long1(location)

# print ("{} has lat and long coordinates of {} and {} ".format (location, geo_lat, geo_long))

def get_weather(address, api_key):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	weather_message = ("In {} the weather is now {} and {}°".format(address, forecast.summary, forecast.temperature))
	return weather_message

#  print (get_weather(address, api_key))

# final_return = get_weather(geo_lat, geo_long, api_key)
# print ("In {} the weather is now {} ".format (location, final_return))



# print ()
# get_location(location)
# get_lat_long(location)
# print (get_weather(location.latitude,location.longitude,api_key)


# Flatiron Building, 175, 5th Avenue, Flatiron, New York, NYC, New York, ...
# print((location.latitude, location.longitude))
# (40.7410861, -73.9896297241625)
# print(location.raw)
# {'place_id': '9167009604', 'type': 'attraction', ...}