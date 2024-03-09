from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/weather')
def weather():
    city = request.args.get('city')  # Get the city from the query parameters
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')
    weather_data = get_weather_data(city, api_key)
    return render_template('weather.html', city=city, weather_data=weather_data)


def get_weather_data(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    return {
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    } if response.ok else None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

# docker build -t weather-app .
# docker run -p 5000:5000 -e OPENWEATHERMAP_API_KEY=daaa8b327f46e48425d2146ae9ec4516 weather-app
