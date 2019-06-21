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

