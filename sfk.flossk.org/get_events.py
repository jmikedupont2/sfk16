import eventbritesecrets
from eventbrite import Eventbrite
eventbrite = Eventbrite(eventbritesecrets.PERSONAL_OAUTH_TOKEN)

# Get my own User ID
my_id = eventbrite.get_user()['id']

# Get a raw list of events (includes pagination details)
events = eventbrite.event_search(**{'user.id': my_id})

import yaml

print yaml.dump(events['events'])

# List the events in draft status
#for x in events['events'] :
#    print yaml.dump(x)
