from flask import Flask, render_template, request
import requests 
import json

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    req = requests.get('api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=6ce765045581e99ca1b61b279625072d')
    json_object = req.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html',temp = temp_f)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)