import json
import os
import glob

source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'
	
for f in glob.glob(source):
	print(f)
	with open(f, 'r') as handle:
		parsed = json.load(handle)

	for i in parsed['topartists']['artist']:
		for f in glob.glob("/home/hans/visProject/api_extract/artistTopTags/"+i['name']+".json"):
		print(i['name'])
