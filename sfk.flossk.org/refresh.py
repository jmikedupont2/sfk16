from bs4 import BeautifulSoup
import re
import unicodedata
import requests
import yaml
import pprint

import eventbritesecrets
from eventbrite import Eventbrite
eventbrite = Eventbrite(eventbritesecrets.PERSONAL_OAUTH_TOKEN)

events = []
# from http://stackoverflow.com/a/1774043/7026063
with open("events.yaml", 'r') as stream:
    try:
        events =yaml.load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        
#print (events)

f = open ('index.html','w')
y = open ('merged.yaml','w')

p = requests.get("http://sfk.flossk.org/sfk16/")
html_doc=p.text
f.write(html_doc)
f.close

soup = BeautifulSoup(html_doc, 'html.parser')


speakers = {}
events2 = {}

for d in soup.find_all('div', class_='speaker'):
    #print ("\n\nSpeaker" + d.h4.text)
    t=d.h4.text
    t=re.sub(r'\s+','_', t)
    t=unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
    name=t.decode('utf-8')
    d['id']="Speaker_" + name

    detail=d.figure.figcaption.a['href']

    p = requests.get("http://sfk.flossk.org/sfk16/" + detail)
    details=p.text
    soup2 = BeautifulSoup(details, 'html.parser')
    #print(d.prettify())    
    #print(soup2.prettify())
    speakers[name] = {
        'header':d.prettify(),
        'details':soup2.prettify()
    }


for e in events:
    n=e['name']['text']
    #events2[n]=e
    g=re.match('([\w\s]+)\s+\-\s+(.+)',n)
    if (g):
        
        (speaker,title)=g.groups()

        event = eventbrite.get_event(e['id'])
        people = eventbrite.get_event_attendees(e['id'])

        #pprint.pprint(event.__dict__)
        events2[title]= {
            'people':  people,
            'eventbrite' : event.__dict__,
            'flossk' : {
                'title' : title,
                'speaker' : speaker
            }
        }

    
for d in soup.find_all('div', class_='event'):
    #print ("Talk: "+ d.h3.text)
    t=d.h3.text

    if t in events2:
        #print ("Talk: "+ t)
        events2[t]['flossk']['html'] = d.prettify()
        t=re.sub(r'\s+','_', t)
        t=unicodedata.normalize('NFKD', t).encode('ascii', 'ignore')
        d['id']="Talk_" + t.decode('utf-8')

        
    else:
        #print ("Missing Talk: "+ t)
        pass
        

    

#print(soup.prettify())
y.write (yaml.dump({
    'speakers' : speakers,
#    'events' :events,
    'events' :events2,
}))
