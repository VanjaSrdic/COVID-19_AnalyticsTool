import requests
import json
import time


# pulling data from the api
def worldwide():
    citizens = 7594
    response = requests.get("https://api.covid19api.com/summary")
    json_response = response.json()
    latest_info = json_response['Global']['TotalConfirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def croatia():
    citizens = 4.058
    response = requests.get("https://api.covid19api.com/total/country/croatia")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def norway():
    citizens = 5.385
    response = requests.get("https://api.covid19api.com/total/country/norway")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def greece():
    citizens = 10.72
    response = requests.get("https://api.covid19api.com/total/country/greece")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def albania():
    citizens = 2.846
    response = requests.get("https://api.covid19api.com/total/country/albania")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def germany():
    citizens = 83.02
    response = requests.get("https://api.covid19api.com/total/country/germany")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def denmark():
    citizens = 5.806
    response = requests.get("https://api.covid19api.com/total/country/denmark")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def hungary():
    citizens = 9.77
    response = requests.get("https://api.covid19api.com/total/country/hungary")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def poland():
    citizens = 37.82
    response = requests.get("https://api.covid19api.com/total/country/poland")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def italy():
    citizens = 60.36
    response = requests.get("https://api.covid19api.com/total/country/italy")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def slovakia():
    citizens = 5.464
    response = requests.get("https://api.covid19api.com/total/country/slovakia")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def france():
    citizens = 66.99
    response = requests.get("https://api.covid19api.com/total/country/france")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def macedonia():
    citizens = 2.077
    response = requests.get("https://api.covid19api.com/total/country/macedonia")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def austria():
    citizens = 8.859
    response = requests.get("https://api.covid19api.com/total/country/austria")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def spain():
    citizens = 46.94
    response = requests.get("https://api.covid19api.com/total/country/spain")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def united_kingdom():
    citizens = 66.65
    response = requests.get("https://api.covid19api.com/total/country/united-kingdom")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def portugal():
    citizens = 10.28
    response = requests.get("https://api.covid19api.com/total/country/portugal")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def sweden():
    citizens = 10.23
    response = requests.get("https://api.covid19api.com/total/country/sweden")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def netherlands():
    citizens = 17.28
    response = requests.get("https://api.covid19api.com/total/country/netherlands")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def serbia():
    citizens = 6.982
    response = requests.get("https://api.covid19api.com/total/country/serbia")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def switzerland():
    citizens = 8.57
    response = requests.get("https://api.covid19api.com/total/country/switzerland")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def belgium():
    citizens = 11.46
    response = requests.get("https://api.covid19api.com/total/country/belgium")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def slovenia():
    citizens = 2.081
    response = requests.get("https://api.covid19api.com/total/country/slovenia")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)

def czechia():
    citizens = 10.69
    response = requests.get("https://api.covid19api.com/total/country/czechia")
    json_response = response.json()
    latest_info = json_response[-1]['Confirmed']
    cases_per_one_mil = float(latest_info)/float(citizens)
    return(cases_per_one_mil)




