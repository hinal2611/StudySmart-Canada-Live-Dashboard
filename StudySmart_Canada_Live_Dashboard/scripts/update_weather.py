import requests
import pandas as pd
from datetime import datetime
from pathlib import Path

# ==============================
# StudySmart Canada Live Dashboard
# Live Weather Data Script
# ==============================

# 1. Add your OpenWeather API key here
API_KEY = "efcfc8f5214a8d40f31048b95d454ef9"

# 2. Canadian cities for your dashboard
cities = [
    "Toronto",
    "Brampton",
    "Vancouver",
    "Calgary",
    "Montreal",
    "Ottawa",
    "Edmonton",
    "Winnipeg",
    "Halifax",
    "Mississauga",
    "Surrey",
    "Hamilton",
    "Quebec City",
    "Saskatoon",
    "Regina"
]

# 3. Store all weather data here
weather_rows = []

# 4. Get live weather data for each city
for city in cities:
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city},CA&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        weather_rows.append({
            "City": city,
            "Temperature": data["main"]["temp"],
            "Feels_Like": data["main"]["feels_like"],
            "Humidity": data["main"]["humidity"],
            "Pressure": data["main"]["pressure"],
            "Weather_Status": data["weather"][0]["description"],
            "Wind_Speed": data["wind"]["speed"],
            "Country": data["sys"]["country"],
            "Latitude": data["coord"]["lat"],
            "Longitude": data["coord"]["lon"],
            "Updated_At": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

        print(f"Data collected for {city}")

    else:
        print(f"Failed to collect data for {city}")
        print("Status Code:", response.status_code)
        print("Message:", response.text)

# 5. Convert data into table format
df = pd.DataFrame(weather_rows)

# 6. Save CSV inside the data folder
output_path = Path(__file__).resolve().parent.parent / "data" / "live_weather.csv"

df.to_csv(output_path, index=False)

# 7. Show final result
print("\nLive weather data updated successfully!")
print("CSV file saved at:", output_path)
print(df)