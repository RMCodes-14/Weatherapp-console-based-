from weather import WeatherApp

def main():
    app = WeatherApp()
    current_unit = "°C"

    print("Welcome to Weather App!")

    while True:
        print(f"\nCurrent unit: {current_unit}")
        print("1. Check Weather by City")
        print("2. Switch Temperature Units")
        print("3. View Search History")
        print("4. Exit")

        choice = input ("Choose an option (1-4): ").strip()

        if choice == "1":
            city = input("Enter City Name: ").strip()
            if not city:
                print(" Please Enter City Name!")
                continue

            print (f"\n Fetching Weather for {city}....")
            weather_data = app.get_weather(city)
            app.display_weather(weather_data , city)

        elif choice == "2":
            current_unit = app.toggle_units()
            print(f"Switched to {current_unit}")

        elif choice == "3":
            app.show_history()

        elif choice == '4':
            print("Thanks for using Weather App! Goodbye!")
            break
        else:
            print("Invalid Choice! Please enter 1-4 ")


if __name__ == "__main__":
    main()
