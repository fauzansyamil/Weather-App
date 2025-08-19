from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "a8e0c30b29d4e5f9698962d6c1f423ef" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather" 

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&units=metric
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None
    
def parse_weather(data):
    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "icon": data["weather"][0]["icon"]
    } 

@app.route('/', methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        data = fetch_weather(city)
        if data:
            weather = parse_weather(data)

    return render_template("index.html", weather=weather)


if __name__ == "__main__":
    app.run(debug=True)