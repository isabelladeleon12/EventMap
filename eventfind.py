import requests
'''response = requests.get(
    #"https://www.eventbriteapi.com/v3/users/me/owned_events/",
    #"https://www.eventbriteapi.com/v3/users/me/owned_events/?expand=organizer,venue",
    "https://www.eventbriteapi.com/v3/events/search/",
    headers = {
        "Authorization": "Bearer DBOS3WZJP4SPLZV6F4BT",
    },
    verify = True,  # Verify SSL certificate
)'''
#print(response.json()['events'][0]['name']['text'])
#print(response.json()['events'])

#should include key and url here
'''
Key: DBOS3WZJP4SPLZV6F4BT
Json of events on my account:
https://www.eventbriteapi.com/v3/users/me/owned_events/?token=DBOS3WZJP4SPLZV6F4BT
'''

#TODO: create method to fetch events near a location that day
#getEvents(location)

def getEvents(lat, lon):
	events = requests.get(
		"https://www.eventbriteapi.com/v3/events/search/?location.latitude=" + str(lat) + "&location.longitude=" + str(lon),
		headers = {
			"Authorization": "Bearer DBOS3WZJP4SPLZV6F4BT",
		},
		verify = True,  # Verify SSL certificate
	)
	event = events.json()['events'][0]
	print(event['name']['text'])

getEvents(37.785227, -122.416889)

