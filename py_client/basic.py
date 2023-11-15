import requests

endpoint = 'https://httpbin.org/anything'

get_response = requests.get(endpoint, json={'query': 'hello world'})

print(get_response.json())
