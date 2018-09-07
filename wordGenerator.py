from random import randint
from requests import get
#from json import json

appID = '0b49baca'
apiKey = '5eea00e14a8f6bd97a21cc70d1c84704'

def generateRandomWord(category):
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/wordlist/en/domains=' + category
    request = get(url, headers = {'app_id': appID, 'app_key': apiKey})
    objects = request.json()['results']
    words = [obj['word'] for obj in objects]
    return words[randint(0, len(words) - 1)]