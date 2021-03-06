import requests

url = 'https://newsapi.org/v2/top-headlines?'

def getArticles(key_phrase, api) :
    
    parameters = {
        'q'         : key_phrase,  
        'pageSize'  : 1,
        'language'  : 'en',            
        'apiKey'    : api        
    }

    response = requests.get(url, params=parameters).json()
    if (response['status'] == 'ok'):
        return response['articles']
    else:
        return {}
