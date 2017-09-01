#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import glob
import pathlib
import sys

source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'
token = 'ba3772fe9087004cadb3715a2f170555'
#url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags'
with open('country_extract.json', 'r') as handle:
	parsed = json.load(handle)

	with open('results.json', 'r') as results:
		parsed_results = json.load(results)

		for i in parsed_results["toptags"]:

			for j in parsed["Countries"]:
				if j["Name"] == i["name"]:
					code = j["Code"]

			total = 0		
			
			try:
				for x in i["tags"]:
					#print(str(list(x.keys())).replace("'", "").replace("[","").replace("]",""))
					if sys.argv[1] in str(list(x.keys())).replace("'", "").replace("[","").replace("]",""): 
						
						value = (str(list(x.values())).replace("[","").replace("]",""))
						total += float(value)
				print("\""+code+"\""+ ": " +  str(total)+",")			
			except Exception as e:
				print(e)
			#print(parsed_results[0]["name"])

		# file = pathlib.Path('artistTopTags/'+i['name']+'.json')
		# temp = url+'&artist='+i['name']+'&api_key='+token+'&format=json'
		# r = requests.get(temp)
		# name = i['name'].replace("/", "")
		# if not file.exists():

		# text_file = open('artistTopTags/'+name+'.json', "w")
		# text_file.write(r.text)
		# text_file.close()