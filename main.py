import news_feed as nf
import weather_feed as wf
import pprint 
import json
from os.path import dirname, abspath, join
from textwrap import wrap
from datetime import date, datetime

path = dirname(dirname(abspath(__file__)))

with open(join(path, 'settings.json'), "r") as f:
    settings = json.load(f)

current_date = date.today()
current_time = datetime.now()
print(current_date.strftime("%d %B, %Y") + " - " + current_time.strftime("%H:%M:%S"))
 
weather_data = wf.getWeather(settings['location'], settings['owmapi-key'])
waether_loc  = weather_data['name']
weather_temp = str(int(weather_data['main']['temp']))
weather_desc = weather_data['weather'][0]['description']

print("{0}: {1}ºc : {2}".format(waether_loc, weather_temp, weather_desc))

print("\n------------------News------------------")

for keyphrase in settings['keyphrases']:
    print("\n" + keyphrase + ":")
    articles = nf.getArticles(keyphrase, settings['newsapi-key'])
    
    for article in articles:
        text = wrap(article['title'], 40)
        for line in text:
            print (line)
        print("({0})".format(article['source']['name']))
