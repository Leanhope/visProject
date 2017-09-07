#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import os.path
#get first 5 top artits from countries and convert to .js dic

f = open('country_extract.json', 'r')
data = f.read()

w = open('topartists.js', 'w')

final = "var topartistiscountry = {\n"

data = json.loads(data)
error = 0

#get all countries from country_extra.json
for i in data:
	code = i["Code"]
	name = i["Name"]
	print(os.path.isfile('geoTopArtists/'+name+'.json'))
	
	#get all countries from *.json
	if os.path.isfile('geoTopArtists/'+name+'.json'):
		f = open('geoTopArtists/'+name+'.json')
		final += "\""+code+"\": { "
		country = f.read()
		#load file as json element
		country = json.loads(country)
		country = country["topartists"]["artist"]
		print("-"+name)
		
		#get the first top artist from country file
		for i in range(0, 5):
			#try if exist
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