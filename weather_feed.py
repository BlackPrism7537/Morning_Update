import requests

url = 'http://api.openweathermap.org/data/2.5/weather?'


def getWeather(location, api):
    parameters = {
        'q' : location,
        'appid' : api,
        'units' : 'metric'
    }

    response = requests.get(url, parameters).json()
    if (response['cod'] == 200):
        return response
    else:
        print(response)
        return {}
