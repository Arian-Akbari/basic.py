import requests

endpoint = 'http://127.0.0.1:8000/'

get_response = requests.get(endpoint, params={'abc': 123}, data={'query': 'hello world'})

# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)
