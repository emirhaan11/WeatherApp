import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta


class GeoRequests:
    def __init__(self, city_name):
        self.city_name = city_name
        load_dotenv(".env")
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        geo_url = "http://api.openweathermap.org/geo/1.0/direct"
        geo_params = {
            "q": city_name,
            "limit": 5,
            "appid": self.api_key
        }
        self.geo_datas = requests.get(geo_url, params = geo_params).json()
        self.lat = self.geo_datas[0]["lat"]
        self.lon = self.geo_datas[0]["lon"]

class FiveDaysRequest(GeoRequests):
    def __init__(self,city_name):
        super().__init__(city_name)

        load_dotenv(".env")
        self.api_key = os.getenv("OPENWEATHER_API_KEY")
        weather_url = "https://api.openweathermap.org/data/2.5/forecast"

        weather_params = {
            "lat" : self.lat,
            "lon" : self.lon,
            "appid" : self.api_key
        }
        self.weather_datas = requests.get(weather_url, params = weather_params).json()
        self.data = self.weather_datas["list"]
        self.today = datetime.strptime(self.data[0]["dt_txt"], "%Y-%m-%d %H:%M:%S").date()

    def get_day_request(self, day_offset):
        target_date = self.today + timedelta(days=day_offset)
        day_data = [entry for entry in self.data if entry["dt_txt"].startswith(str(target_date))]

        if not day_data:
            return None

        max_temp = max(day_data, key=lambda x: x["main"]["temp_max"])
        min_temp = min(day_data, key=lambda x: x["main"]["temp_min"])

        return {
            "date": target_date.strftime("%A"),
            "max_temp": int(max_temp["main"]["temp_max"]-273.15),
            "min_temp": int(min_temp["main"]["temp_min"]-273.15),
            "humidity": max_temp["main"]["humidity"],
            "max_temp_icon": max_temp["weather"][0]["icon"],
            "min_temp_icon": min_temp["weather"][0]["icon"]
        }

    def get_today_request(self):
        return self.get_day_request(0)

    def get_secondDday_request(self):
        return self.get_day_request(1)

    def get_thirdDay_request(self):
        return self.get_day_request(2)

    def get_fourthDay_request(self):
        return self.get_day_request(3)

    def get_fifthDay_request(self):
        return self.get_day_request(4)

    def get_sixthDay_request(self):
        return self.get_day_request(5)


if __name__ == "__main__":
    try:
        weather = FiveDaysRequest("Ankara")
        print(weather.get_secondDday_request())
    except Exception as e:
        print(f"Error: {e}")

