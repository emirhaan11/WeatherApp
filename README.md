# 🌤️ CustomTkinter Weather App
This project is my first experience using the python API, it is a Python application that displays the weather forecasts of cities using the CustomTkinter and [*OpenWeather*](https://openweathermap.org/) API. The application shows the five-day weather forecast with temperature, humidity and weather icons.

## 🚀 Features
- Displays the weather forecast for a user-entered city
- Provides a five-day forecast
- Shows daily maximum and minimum temperatures
- Includes humidity information
- Displays weather condition icons

## 🖼️ Screenshots
![Ekran görüntüsü 2025-02-19 123001](https://github.com/user-attachments/assets/7fc022a6-10e2-4984-9b11-174d03ba08e7)
![Ekran görüntüsü 2025-02-19 123020](https://github.com/user-attachments/assets/56b13160-c491-4f42-8478-9026438e589c)

## 📥 Installation & Usage

1. Clone the project:
 - `git clone https://github.com/emirhaan11/WeatherApp.git`
 - `cd weather-app`

2. Install dependencies:
 - `pip install -r requirements.txt`

3. Add your API key:
- You need an API key from OpenWeather to use this application.
- Create a .env file in the project directory and add the following line:
   - `OPENWEATHER_API_KEY=your_api_key_here`

4. Run the application:
 - `python main.py`

## 🔑 API Key Usage

This application works with the **OpenWeather API**. To get your **API key**:

1. Visit [OpenWeather](https://openweathermap.org/).
2. Sign up and obtain your API key.
3. Add it to the .env file.

## 📌 Dependencies
- os
- requests
- Pillow
- customtkinter
- dotenv
- datetime

To install all dependencies, run:

`pip install -r requirements.txt`

