
import requests

API_KEY = "cbdab0bee5f640f10c7429430cc3ff63"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=15)
    data = response.json()

    if response.status_code == 200:
        print("\n=== Current Weather ===")
        print("City:", data["name"])
        print("Weather:", data["weather"][0]["description"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
    else:
        print("Error:", data.get("message", "Unable to get weather"))

except requests.RequestException as error:
    print("Network error:", error)
