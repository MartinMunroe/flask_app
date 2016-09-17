from flask import Flask, render_template, request, app
app = Flask(__name__)

import forecastio
from geopy.geocoders import Nominatim
import os
# from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api_key = os.environ['WEATHER_API']


def get_weather(address, api_key):
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	weather_message = ("In {} the weather is now {} and {}°".format(address, forecast.summary, forecast.temperature))
	return weather_message

@app.route('/')
def index():
    name = request.values.get('name')
    city = request.values.get('city')
    return render_template('index.html', name=name, city=city, weather =get_weather(city,api_key)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/weath_box')
def weath_box():
	return render_template('weath_box.html')

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

# import os
# from intro_to_flask import app

# port = int(os.environ.get("PORT", 5000))
# app.run(debug=True, host='0.0.0.0', port=port)


