from bs4 import BeautifulSoup
import re
import unicodedata

import yaml

events = {}
# from http://stackoverflow.com/a/1774043/7026063
with open("merged.yaml", 'r') as stream:
    try:
        events =yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)

import eventbritesecrets
from eventbrite import Eventbrite
eventbrite = Eventbrite(eventbritesecrets.PERSONAL_OAUTH_TOKEN)

# Get my own User ID
my_id = eventbrite.get_user()['id']



import requests
import logging

def debug_request():
    try:
        import http.client as http_client
    except ImportError:
        # Python 2
        import httplib as http_client
    http_client.HTTPConnection.debuglevel = 1

    # You must initialize logging, otherwise you'll not see debug output.
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


# Get a raw list of events (includes pagination details)
import pprint
#pprint.pprint(events['events2'])
import re

#def update(event, ed):

for e in events['events2'].keys():
    ed = events['events2'][e]
    eventid = ed['id']
    print (e,eventid)
    #pprint.pprint( ed['html'])

    # g=re.match('([\w\s])+\-\s+(.+)',e)
    # if (g):
    #     (speaker,title)=g.groups()
    #     #print (title)
    #     events2[title]=e
    #     events2[title]['speaker']=speaker

    #ed['speaker']=
    event = eventbrite.get_event(eventid)
    #print ("event data:-------------------------------")
    #pprint.pprint( event)
    #update(event,ed)
    if (not event['description']['html']) and ('html' in ed):
        #event['description']['html']= ed['html']
        #event['description']['text']= 'test'
        #eventbrite.post_event(event)
        event2 = {
            'event.description.html' : ed['html'],
            'event.category_id': u'102',
            'event.subcategory_id': '2004'        
        }
        pprint.pprint(eventbrite.post("/events/" + eventid + "/", data=event2))

        event = eventbrite.get_event(eventid)

        #pprint.pprint( event)

        #exit(0)
    print ("event : " + e  + " : " + event['url'])
    #print ("-------------------------------------------")

    
