#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import os.path

f = open('country_extract.json', 'r')
data = f.read()

w = open('topartists.js', 'w')

final = "var topartistiscountry = {\n"

data = json.loads(data)
error = 0
limit = '3'
token = 'ba3772fe9087004cadb3715a2f170555'
url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists' #geoArtists
#url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks' #geoTracks
#http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=Albania&api_key=ba3772fe9087004cadb3715a2f170555&format=json&limit=25


for i in data:
	code = i["Code"]
	name = i["Name"]
	print(os.path.isfile('geoTopArtists/'+name+'.json'))
	
	if os.path.isfile('geoTopArtists/'+name+'.json'):
		f = open('geoTopArtists/'+name+'.json')
		final += "\""+code+"\": { "
		country = f.read()
		country = json.loads(country)
		country = country["topartists"]["artist"]
		print("-"+name)
		
		for i in range(0, 5):
			try:
				artist = country[i]["name"]
				listeners = country[i]["listeners"]
				url = country[i]["url"]
				img = country[i]["image"][2]["#text"]
				final += str(i) + ":{ \"artist\": \""+ artist +"\", \"listeners\": "+listeners+", \"url\": \""+url+"\", \"img\": \""+img+"\" },\n"
				error = 0
			except Exception as e:
				print(e)
				error = 1

	if os.path.isfile('geoTopArtists/'+name+'.json') or error == 1:
		final += "},\n"

final += "}"

w.write(final)
w.close()