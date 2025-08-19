🌤️ Weather App with Flask

A simple web application built with **Flask** that allows users to check the current weather of any city using the OpenWeather API.

🚀 Features
- Search weather by city name
- Display temperature, humidity, and weather description
- Responsive and simple UI with HTML + CSS
- Built with Python (Flask) and OpenWeather API

📚 Tech Stack
- Backend: Python (Flask)
- Frontend: HTML, CSS
- API: OpenWeather API

weather-app/
│── app.py              
│── templates/         
│   └── index.html
│── static/            
│── requirements.txt    
│── README.md           

🛠️ Installation & Setup
1. Clone the repository:
   git clone https://github.com/fauzansyamil/weather-app.git
   cd Weather App

2. Create virtual environment & install dependencies:
    python -m venv venv
    source venv/bin/activate   # for Linux/Mac
    venv\Scripts\activate      # for Windows
    pip install -r requirements.txt

3. Add your OpenWeather API key in app.py:
    API_KEY = "YOUR_API_KEY"

4. Run the app:
    cd WeatherFlask
    python app.py

5. Open in browser:
    http://127.0.0.1:5000/


