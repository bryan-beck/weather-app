import requests

def get_weather_desc_and_temp():
    api_key = "0ba733e09ba25656f950bb7c5c5e6449"
    city = "Orlando"
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {'description': description,
            'temp_min': temp_min,
            'temp_max': temp_max}
# print the results
weather_dict = get_weather_desc_and_temp()
print("today's forecast is", weather_dict.get('description'))
print("the minimum temperature is", weather_dict.get('temp_min'))
print("the maximum temperature is", weather_dict.get('temp_max'))
