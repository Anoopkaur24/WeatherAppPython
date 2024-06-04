import requests

API_KEY = '7db1484d9a1081aa70110ae92f598511'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
def get_weather(city):
    # Construct the complete API URL
    url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
    # Send a GET request to the API
    response = requests.get(url)
    # Parse the JSON data from the response
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]

        # Extract the relevant data
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        weather_description = weather["description"]
        wind_speed = wind["speed"]

        # Display the weather information
        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Weather: {weather_description.capitalize()}")
        print(f"Wind Speed: {wind_speed} m/s")
        print("---------------------------")
    else:
        print(f"City {city} not found.")
        print("---------------------------")


if __name__ == "__main__":
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        get_weather(city)
