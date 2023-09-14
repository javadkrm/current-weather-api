from current_temp_api.main import OpenMeteo,OpenWeather
open_meteo_obj = OpenMeteo(32,53)
temp = open_meteo_obj.get_current_temperature()
print(temp)

open_weather_obj = OpenWeather(32,53,api_token = "ffcfd2f420d7e9e4625ef01f13f61380")
temp2 = open_weather_obj.get_current_temperature()
temp2_c = temp2 - 273.15
print(temp2_c,"celsius")