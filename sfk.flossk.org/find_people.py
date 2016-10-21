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



# Get a raw list of events (includes pagination details)
import pprint
#pprint.pprint(events['events2'])
import re



for e in events['events'].keys():
    ed = events['events'][e]
    for x in ed['people']['attendees']:
        #print (x)
        print (x['profile']['name'],"\t",x['profile']['email'])
    #['people']
    
    
