#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import glob
import pathlib

source = 'api_extract/geoTopArtists/*.json'
token = 'ba3772fe9087004cadb3715a2f170555'
url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags'
	
for f in glob.glob(source):
	print(f)
	with open(f, 'r') as handle:
		parsed = json.load(handle)

	for i in parsed['topartists']['artist']:
		
		file = pathlib.Path('artistTopTags/'+i['name']+'.json')
		temp = url+'&artist='+i['name']+'&api_key='+token+'&format=json'
		r = requests.get(temp)
		name = i['name'].replace("/", "")
		if not file.exists():
			text_file = open('artistTopTags/'+name+'.json', "w")
			text_file.write(r.text)
			text_file.close()