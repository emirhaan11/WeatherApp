import os
from PIL import Image
import customtkinter as ctk
from request_data import FiveDaysRequest


class WeatherApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Weather App")
        self.geometry("400x350")
        self.resizable(False,False)
        ctk.set_appearance_mode("light")

        self.create_widgets()

    def create_widgets(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.title_label = ctk.CTkLabel(self.main_frame, text="Weather Forecast", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=10)

        self.city_entry = ctk.CTkEntry(self.main_frame, placeholder_text="ENTER CITY NAME", font=("Arial", 14, "bold"))
        self.city_entry.pack(pady=10)
        self.city_entry.bind("<Return>", lambda event: self.get_weather())

        self.get_weather_button = ctk.CTkButton(self.main_frame, text="Get Weather Forecast",
                                                font=("Arial", 14, "bold"), command=self.get_weather)
        self.get_weather_button.pack(pady=10)

        self.result_frame = ctk.CTkFrame(self.main_frame)
        self.result_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.days_labels = []
        self.humidity_labels = []
        self.max_icon_labels = []
        self.min_icon_labels = []
        self.temp_labels = []

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for day in days:
            row_frame = ctk.CTkFrame(self.result_frame)
            row_frame.pack(fill="x", padx=5, pady=2)

            day_label = ctk.CTkLabel(row_frame, text=day, font=("Arial", 14, "bold"))
            day_label.pack(side="left", padx=5)

            temp_label = ctk.CTkLabel(row_frame, text="- / - °C", font=("Arial", 14))
            temp_label.pack(side="right", padx=10)

            maxicon_label = ctk.CTkLabel(row_frame, text="")
            maxicon_label.pack(side="right", padx=5)

            minicon_label = ctk.CTkLabel(row_frame, text="")
            minicon_label.pack(side="right", padx=5)

            humidity_label = ctk.CTkLabel(row_frame, text="--%", font=("Arial", 12))
            humidity_label.pack(side="right", padx=15)



            self.days_labels.append(day_label)
            self.humidity_labels.append(humidity_label)
            self.max_icon_labels.append(maxicon_label)
            self.min_icon_labels.append(minicon_label)
            self.temp_labels.append(temp_label)

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            weather = FiveDaysRequest(city)
            forecast_data = [
                weather.get_today_request(),
                weather.get_secondDday_request(),
                weather.get_thirdDay_request(),
                weather.get_fourthDay_request(),
                weather.get_fifthDay_request()
            ]

            for i in range(5):
                if forecast_data[i]:
                    max_temp = int(forecast_data[i]['max_temp'])
                    min_temp = int(forecast_data[i]['min_temp'])
                    min_icon_code = forecast_data[i]['min_temp_icon']
                    max_icon_code = forecast_data[i]["max_temp_icon"]
                    humidity = forecast_data[i]["humidity"]

                    self.temp_labels[i].configure(text=f"{max_temp}°C / {min_temp}°C")
                    self.humidity_labels[i].configure(text=f"{humidity}%")

                    max_icon_path = f"images/{max_icon_code}.png"
                    min_icon_path = f"images/{min_icon_code}.png"

                    if os.path.exists(max_icon_path):
                        image = ctk.CTkImage(Image.open(max_icon_path), size=(30, 30))
                        self.max_icon_labels[i].configure(image=image, text="")
                        self.max_icon_labels[i].image = image

                    if os.path.exists(min_icon_path):
                        image = ctk.CTkImage(Image.open(min_icon_path), size=(30, 30))
                        self.min_icon_labels[i].configure(image=image, text="")
                        self.min_icon_labels[i].image = image

        else:
            for label in self.temp_labels:
                label.configure(text="- / - °C")
            for label in self.humidity_labels:
                label.configure(text="--%")
            for icon in self.max_icon_labels:
                icon.configure(text="")
            for icon in self.min_icon_labels:
                icon.configure(text="")


if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
