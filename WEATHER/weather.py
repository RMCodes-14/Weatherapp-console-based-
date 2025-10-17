import requests
from config import API_KEY , BASE_URL

class WeatherApp:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = BASE_URL
    
    def get_weather( self, city_name):
        """Get weaather data for city"""
        params = {
            'q' :city_name ,
            'appid' : self.api_key,
            'units' : 'metric'

        }
        try:
            response = requests.get(self.base_url, params = params)
            response.raise_for_status()

            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data {e}")
            return None
        