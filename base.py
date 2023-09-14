from abc import ABC,abstractmethod
import requests

class weatherAPIBase(ABC):
    def __init__(self,latitude,longitude,**kwargs):
        self.latitude = latitude
        self.longitude = longitude

    def get_current_temperature(self):
        pass
        #params = {"longitude":self.longitude,"latitude":self.latitude,"current_weather":True}
        #result = requests.get("https://api.open-meteo.com/v1/forecast",params=params)
        #result_jason = result.json()
        #return result_jason["current_weather"]["temperature"]     