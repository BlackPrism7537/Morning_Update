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
    data = "{} - {}".format(current_date.strftime("%d %B, %Y"),current_time.strftime("%H:%M:%S"))
    print("{:^40}".format(data))
 

def weather():
    weather_data = getWeather(settings['location'], settings['owmapi-key'])
    waether_loc  = weather_data['name']
    weather_temp = int(weather_data['main']['temp'])
    weather_desc = weather_data['weather'][0]['description']

    data = "{0} : {1} : {2}ºc".format(waether_loc, weather_desc, weather_temp)
    print("{:^40}".format(data))


def todoList():
    with open(settings['todo-json'], "r") as f:
        tasks = load(f)['tasks']

    print("\n------------------Todo------------------\n")

    for task in tasks:
        print("{0:<35.35} : ☐".format(task))


def news():
    print("\n------------------News------------------")

    for keyphrase in settings['keyphrases']:
        article = getArticles(keyphrase, settings['newsapi-key'])
        if (article):
            print("\n" + keyphrase + ":")
            text = wrap(article[0]['title'], 40)
            for line in text:
                print(line)
            print("({0})".format(article[0]['source']['name']))


if __name__ == "__main__":
    time()
    weather()
    todoList()
    news()
    