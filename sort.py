import countries
import numpy as np
import requests
import json
import time

worldwide = int(countries.worldwide())
croatia = int(countries.croatia())
norway = int(countries.norway())
greece = int(countries.greece())
albania = int(countries.albania())
germany = int(countries.germany())
time.sleep(5)
denmark = int(countries.denmark())
hungary = int(countries.hungary())
poland = int(countries.poland())
italy = int(countries.italy())
slovakia = int(countries.slovakia())
time.sleep(5)
france = int(countries.france())
macedonia = int(countries.macedonia())
austria = int(countries.austria())
spain = int(countries.spain())
united_kingdom = int(countries.united_kingdom())
portugal = int(countries.portugal())
sweden = int(countries.sweden())
netherlands = int(countries.netherlands())
serbia = int(countries.serbia())
switzerland = int(countries.switzerland())
time.sleep(5)
belgium = int(countries.belgium())
slovenia = int(countries.slovenia())
czechia = int(countries.czechia())

ukupno = [{ "name" : "Worldwide: ", "cases" : worldwide, "hrv" : "Cijeli svijet: ", "ger" : "Weltweit: ", "ita" :"Nel mondo: ", "slo" : "Po vsem svetu: "}] 

lis = [
{ "name" : "Croatia: ", "cases" : croatia, "hrv" : "Hrvatska: ", "ger" : "Kroatien: ", "ita" :"Croazia: ", "slo" : "Hrvaška: "}, 
{ "name" : "Albania: ", "cases" : albania, "hrv" : "Albania: ", "ger" : "Albanien: ", "ita" :"Albania: ", "slo" : "Albanija: " },
{ "name" : "Norway: ", "cases" : norway, "hrv" : "Norveška: ", "ger" : "Norwegen: ", "ita" :"Norvegia: ", "slo" : "Norveška: " },
{ "name" : "Greece: ", "cases" : greece, "hrv" : "Grčka: ", "ger" : "Griechenland: ", "ita" :"Grecia: ", "slo" : "Grčija: " },
{ "name" : "Germany: ", "cases" : germany, "hrv" : "Njemačka: ", "ger" : "Deutschland: ", "ita" :"Germania: ", "slo" : "Nemčija: " },
{ "name" : "France: " , "cases" : france, "hrv" : "Francuska: ", "ger" : "Frankreich: ", "ita" :"Francia: ", "slo" : "Francija: " },
{ "name" : "Denmark: " , "cases" : denmark, "hrv" : "Danska: ", "ger" : "Danimarca: ", "ita" :"Danimarca: ", "slo" : "Danska: " },
{ "name" : "Hungary: " , "cases" : hungary, "hrv" : "Mađarska: ", "ger" : "Ungarn: ", "ita" :"Ungheria: ", "slo" : "Madžarska: " },
{ "name" : "Poland: " , "cases" : poland, "hrv" : "Poljska: ", "ger" : "Polen: ", "ita" :"Polonia: ", "slo" : "Poljska: " },
{ "name" : "Italy: " , "cases" : italy, "hrv" : "Italija: ", "ger" : "Italien: ", "ita" :"Italia: ", "slo" : "Italija: " },
{ "name" : "Slovakia: " , "cases" : slovakia, "hrv" : "Slovačka: ", "ger" : "Slowakei: ", "ita" :"Slovacchia: ", "slo" : "Slovaška: " },
{ "name" : "Macedonia: " , "cases" : macedonia, "hrv" : "Makedonija: ", "ger" : "Mazedonien: ", "ita" :"Macedonia: ", "slo" : "Makedonija: " },
{ "name" : "Austria: " , "cases" : austria, "hrv" : "Austrija: ", "ger" : "Österreich: ", "ita" :"Austria: ", "slo" : "Avstrija: " },
{ "name" : "Spain: " , "cases" : spain, "hrv" : "Španjolska: ", "ger" : "Spanien: ", "ita" :"Spagna: ", "slo" : "Španija: " },
{ "name" : "United Kingdom: " , "cases" : united_kingdom, "hrv" : "Ujedinjeno Kraljevstvo: ", "ger" : "Združeno kraljestvo: ", "ita" :"Regno Unito: ", "slo" : "Združeno kraljestvo: " },
{ "name" : "Portugal: " , "cases" : portugal, "hrv" : "Portugal: ", "ger" : "Portugal: ", "ita" :"Portogallo: ", "slo" : "Portugalska: " },
{ "name" : "Sweden: " , "cases" : sweden, "hrv" : "Švedska: ", "ger" : "Schweden: ", "ita" :"Svezia: ", "slo" : "Švedska: " },
{ "name" : "Netherlands: " , "cases" : netherlands, "hrv" : "Nizozemska: ", "ger" : "Niederlande: ", "ita" :"Olanda: ", "slo" : "Nizozemska: " },
{ "name" : "Serbia: " , "cases" : serbia, "hrv" : "Srbija: ", "ger" : "Serbien: ", "ita" :"Serbia: ", "slo" : "Srbija: " },
{ "name" : "Switzerland: " , "cases" : switzerland, "hrv" : "Švicarska: ", "ger" : "Schweiz: ", "ita" :"Belgio: ", "slo" : "Belgija: " },
{ "name" : "Belgium: " , "cases" : belgium, "hrv" : "Belgija: ", "ger" : "Belgien: ", "ita" :"Belgio: ", "slo" : "Belgija: " },
{ "name" : "Slovenia: " , "cases" : slovenia, "hrv" : "Slovenija: ", "ger" : "Slowenien: ", "ita" :"Slovenia: ", "slo" : "Slovenija: "},
{ "name" : "Czechia: " , "cases" : czechia, "hrv" : "Češka: ", "ger" : "Tschechien: ", "ita" :"Repubblica Ceca: ", "slo" : "Češka: " },]

sorted = sorted(lis, key = lambda i: i['cases'])


