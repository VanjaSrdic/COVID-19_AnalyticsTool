import countries
import numpy as np
import requests
import json
import time

#istra = input("input istria: ")

#istria = countries.istria(istra)
croatia = countries.croatia()
norway = countries.norway()
greece = countries.greece()
albania = countries.albania()
germany = countries.germany()
denmark = countries.denmark()
hungary = countries.hungary()
poland = countries.poland()
italy = countries.italy()
slovakia = countries.slovakia()
time.sleep(5)
france = countries.france()
macedonia = countries.macedonia()
austria = countries.austria()
spain = countries.spain()
united_kingdom = countries.united_kingdom()
portugal = countries.portugal()
sweden = countries.sweden()
netherlands = countries.netherlands()
serbia = countries.serbia()
switzerland = countries.switzerland()
time.sleep(5)
belgium = countries.belgium()
slovenia = countries.slovenia()
czechia = countries.czechia()

#countries_array = [croatia, norway, greece, albania, germany, denmark, hungary, poland, italy, slovakia, france, macedonia, austria, spain, united_kingdom, portugal, sweden, netherlands, serbia, switzerland, belgium, slovenia, czechia]

def sort(to_sort):
    for i in range(len(to_sort)):
        swap = i + np.argmin(to_sort[i:]) 
        (to_sort[i], to_sort[swap]) = (to_sort[swap], to_sort[i])
    return(to_sort)



lis = [{ "ime" : "Hrvatska", "cases" : croatia}, 
{ "ime" : "Albania", "cases" : albania },
{ "ime" : "Norway", "cases" : norway },
{ "ime" : "Greece", "cases" : greece },
{ "ime" : "Germany", "cases" : germany },
{ "ime" : "Albania", "cases" : albania },
{ "ime" : "France" , "cases" : france }]
 
# using sorted and lambda to print list sorted
# by age 
print("The list printed sorting by age: ")
print(sorted(lis, key = lambda i: i['cases']))
 