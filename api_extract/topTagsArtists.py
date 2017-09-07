#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import os
import glob

#get for all top 5 artists per country the top 10 tags. This helps to visualize the bubble chart

url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags&api_key=ba3772fe9087004cadb3715a2f170555&format=json' #geoArtists
patha = "geoTopArtists/*.json"
patht = "artistTopTags/"
final = str()


#get the top artist files per country
for f in glob.glob(patha):
	final += "id,value\ntag,\n"
	
	country = f.split('/')
	country = country[1].split('.')
	country = country[0]
	
	countrylist = open("country_extract.json")
	countrylist = countrylist.read()
	countrylist = json.loads(countrylist)

	#get countries and codes for linking
	for i in countrylist:
		code = i["Code"]
		name = i["Name"]

		#create .csv file for saving
		if country == name:
			w = open("topTagsArtistsCountries/"+code+".csv", 'w')
			

	with open(f, 'r') as handle:
		parsed = json.load(handle)
		print(f)
	
	#get top 5 tags from artistTopTag.json
	for i in range(0, 5):
		try:
			artist = parsed["topartists"]["artist"][i]["name"]
			final += "tag."+artist+",\n"

			tagfile = open(patht+artist+".json")
			tagfile = tagfile.read()
			tagfile = json.loads(tagfile)

			#create sting
			for i in range(0, 10):
				tag = tagfile["toptags"]["tag"][i]["name"]
				count = tagfile["toptags"]["tag"][i]["count"]
				final += "tag."+artist+"."+tag+","+str(count)+"\n"
	
		except Exception as e:
			print(e)
	#try to write if file exists
	try:
		w.write(final)
		final = str()			
		w.close()	
	except Exception as e:
		print(e)
		w.close()


