import requests

from datetime import datetime
from flask import Flask, redirect, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/time')

@app.route('/ip')
def ip():
    return jsonify({
        'ip': request.remote_addr,
    })

@app.route('/time')
def time():
    return jsonify({
        'current_time': datetime.now(),
    })

@app.route('/weather/<string:city>')
def weather(city):
    # Using a test API key here for the sake of example.
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",
                            {'q': city, 'appid': '4a48e1e1428fd83889074671fbf259d9'})

    data = response.json()
    return jsonify({
        'city': data["name"],
        'weather': data["weather"][0]["description"],
    })

