from abc import ABC,abstractmethod
import requests

class weatherAPIBase(ABC):
    def __init__(self,latitude,longitude,**kwargs):
        self.latitude = latitude
        self.longitude = longitude
    @abstractmethod
    def get_current_temperature(self):
        pass