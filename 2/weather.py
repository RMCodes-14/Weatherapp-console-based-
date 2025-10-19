import requests
from config import API_KEY , BASE_URL

class WeatherApp:
    def __init__(self):
        self.api_key  = API_KEY
        self.base_url = BASE_URL
        self.search_history = [] # Track searched cities
        self.unit = 'metric'     # Default: Celsius

    def get_weather(self, city_name):
        '''Get weather data for a city with better error handling'''
        params ={
            'q' : city_name,
            'appid' : self.api_key,
            'units' : self.unit
            }
        try:
            response = requests.get(self.base_url , params = params)
            data = response.json()
            if response.status_code == 200:
            # Add to search history
                if city_name not in self.search_history:
                    self.search_history.append(city_name)
                return data
            else:
                error_msg = data.get('message' , 'Unknown error')
                if response.status_code == 404:
                    return f"City {city_name} not found.Check spelling!"
                elif response.status_code == 401:
                    return "Invalid Api Key. Please check configuration."
                else:
                    return f"Api Error: {error_msg}"
            
        except requests.exceptions.ConnectionError:
            return "Network error: Please check your internet connection"
        except requests.exceptions.Timeout:
            return "Request Timeout: Please try again"
        except Exception as e:
            return f"Unexpected Error: {e}"

    def toggle_units(self):
        '''Switch between Celcius and Farenhiet'''

        if self.unit == 'metric':
            self.unit = 'imperial'
            return "°F"
        else:
            self.unit = 'metric'
            return "°C"
        
    def display_weather(self , weather_data , city):
        if isinstance (weather_data , str):
            print(weather_data)
            return   
        
        unit_symbol = "°C" if self.unit == 'metric' else "°F"

        print(f"\n Weather in {city.upper()}")
        print(f"Temperature: {weather_data['main']['temp']}{unit_symbol}")
        print(f"Feels Like: {weather_data['main']['feels_like']}{unit_symbol}")
        print(f"Description: {weather_data['weather'][0]['description'].title()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Pressure: {weather_data['main']['pressure']} hPa")
     
    def show_history(self):
        if not self.search_history:
            print("No cities searched yet!")
            return
        print("\n Search History: ")
        for i , city in enumerate (self.search_history [-5:] , 1): #Last 5 cities
            print(f" {i}. {city}")

       
  
