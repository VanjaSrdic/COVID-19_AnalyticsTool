import requests
import json

def france():
    citizens = 66.99
    response = requests.get("https://api.covid19api.com/total/country/france")
    json_response = response.json()
    return(json_response)

print(france())