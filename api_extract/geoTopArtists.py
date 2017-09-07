#coding: utf8
import urllib
import json
from collections import namedtuple
import requests

#get 200 topartists from each country from last.fm


f = open('country_extract.json', 'r')
data = f.read()

data = json.loads(data)

limit = '200'
token = 'ba3772fe9087004cadb3715a2f170555'
url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists'

for i in data:
	print(i['Name'])

	#define url
	temp = url+'&country='+i['Name']+'&api_key='+token+'&format=json&limit='+limit
	#send request to last.fm
	r = requests.get(temp)
	print(r.text)
	
	#sace data
	text_file = open('geoTopArtists/'+i['Name']+'.json', "w")
	text_file.write(r.text)
	text_file.close()
	


