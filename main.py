import requests
from base import weatherAPIBase

class OpenMeteo(weatherAPIBase):
    def __init__(self,latitude,longitude,**kwargs):
        self.latitude = latitude
        self.longitude = longitude
    def get_current_temperature(self):
        params = {"longitude":self.longitude,"latitude":self.latitude,"current_weather":True}
        result = requests.get("https://api.open-meteo.com/v1/forecast",params=params)
        result_jason = result.json()
        return result_jason["current_weather"]["temperature"]
class OpenWeather(weatherAPIBase):
    def __init__(self, latitude, longitude,**kwargs):
        self.latitude = latitude
        self.longitude = longitude
        self.api_token = kwargs.get("api_token")
 
    def get_current_temperature(self):
        params = {"lon":self.longitude,"lat":self.latitude,"appid":self.api_token}

        result = requests.get("https://api.openweathermap.org/data/2.5/weather",params=params)
        result_jason = result.json()
        return result_jason["main"]["temp"]    





if __name__ =="__main__":
    open_meteo_obj = OpenMeteo(32,53)
    temp = open_meteo_obj.get_current_temperature()
    print(temp)

    open_weather_obj = OpenWeather(32,53,api_token = "ffcfd2f420d7e9e4625ef01f13f61380")
    temp2 = open_weather_obj.get_current_temperature()
    temp2_c = temp2 - 273.15
    print(temp2_c,"celsius")