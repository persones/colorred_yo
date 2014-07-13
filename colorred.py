import urllib2
import json
from time import sleep
import requests
from my_token import yo_api_token

api_token= yo_api_token() # this is my api key
url = "http://www.oref.org.il/WarningMessages/alerts.json" #homefront command alerts

lastState = False
state = False

while True:
    try:
        res = urllib2.urlopen(url).read()
        json2 = json.loads(unicode(res, 'utf-16'))
        if len(json2["data"]) > 0: # we're looking for the moment we change for having no alarms to any number of alarms.
            state = True
        else:
            state = False
        if state and not lastState:
            requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token}) #this is how you YO all your sunscribers
        lastState = state
    except:
        pass    
    sleep(2)