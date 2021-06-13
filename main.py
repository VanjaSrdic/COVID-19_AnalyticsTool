#THIS FILE HAS TO BE RUN FOR THE CODE TO BE EXECUTED PROPERLY
import sort

i = 0
# fetching the right data and lnguage presets
print(sort.ukupno[0]["hrv"], sort.ukupno[0]["cases"])
while i < len(sort.sorted):
    print(sort.sorted[i]["hrv"], sort.sorted[i]["cases"])
    i += 1

print("")
i = 0

print(sort.ukupno[0]["name"], sort.ukupno[0]["cases"])
while i < len(sort.sorted):
    print(sort.sorted[i]["name"], sort.sorted[i]["cases"])
    i += 1

print("")
i = 0

print(sort.ukupno[0]["ger"], sort.ukupno[0]["cases"])
while i < len(sort.sorted):
    print(sort.sorted[i]["ger"], sort.sorted[i]["cases"])
    i += 1

print("")
i = 0

print(sort.ukupno[0]["ita"], sort.ukupno[0]["cases"])
while i < len(sort.sorted):
    print(sort.sorted[i]["ita"], sort.sorted[i]["cases"])
    i += 1

print("")
i = 0

print(sort.ukupno[0]["slo"], sort.ukupno[0]["cases"])
while i < len(sort.sorted):
    print(sort.sorted[i]["slo"], sort.sorted[i]["cases"])
    i += 1