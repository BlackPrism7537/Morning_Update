from json import load
from weather_feed import getWeather
from news_feed import getArticles
from os.path import dirname, abspath, join
from textwrap import wrap
from datetime import datetime

with open(join(dirname(abspath(__file__)), 'settings.json'), "r") as f:
    settings = load(f)


def time():
    current_date = datetime.today()
    current_time = datetime.now()
    print(current_date.strftime("%d %B, %Y") + " - " + current_time.strftime("%H:%M:%S"))
 

def weather():
    weather_data = getWeather(settings['location'], settings['owmapi-key'])
    waether_loc  = weather_data['name']
    weather_temp = int(weather_data['main']['temp'])
    weather_desc = weather_data['weather'][0]['description']

    print("{0}: {1}ºc : {2}".format(waether_loc, weather_temp, weather_desc))


def news():
    print("\n------------------News------------------")

    for keyphrase in settings['keyphrases']:
        print("\n" + keyphrase + ":")
        articles = getArticles(keyphrase, settings['newsapi-key'])
        
        for article in articles:
            text = wrap(article['title'], 40)
            for line in text:
                print (line)
            print("({0})".format(article['source']['name']))


if __name__ == "__main__":
    time()
    weather()
    news()
    