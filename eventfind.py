import requests
response = requests.get(
    "https://www.eventbriteapi.com/v3/users/me/owned_events/",
    headers = {
        "Authorization": "Bearer DBOS3WZJP4SPLZV6F4BT",
    },
    verify = True,  # Verify SSL certificate
)
print(response.json()['events'][0]['name']['text'])