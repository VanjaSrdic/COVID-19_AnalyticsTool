import requests
import json

response = requests.get("https://api.covid19api.com/summary")
json_response = response.json()
dictio = json.dumps(json_response)
dictionary = json.loads(dictio)
print(dictionary)