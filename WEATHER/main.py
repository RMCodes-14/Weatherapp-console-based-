from weather import WeatherApp

def main():
    app = WeatherApp()

    print("Welcome to Weather App! ")

    while True:
        city = input("\nEnter city name (or 'quit' to exit: )").strip()

        if city.lower() =='quit':
            print("GOODBYE! ")
            break

        if not city:
            print("Please enter city name!")
            continue

        weather_data = app.get_weather(city)

        if weather_data:
            print(f"\n Weather in {city}: ")
            print(f"\n Temperature: {weather_data['main']['temp']}°C")
            print(f"\n Description: {weather_data['weather'][0]['description']}")
            print(f"\n Humidity: {weather_data['main']['humidity']}%")
            print(f"\n Wind Speed: {weather_data['wind']['speed']}m/s")

if __name__ =="__main__":
    main()

