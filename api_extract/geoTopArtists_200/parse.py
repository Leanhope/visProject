import json
import os
import glob

counter = 0
source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'
	
for f in glob.glob(source):
	print(f)
	counter += 1
	print(counter)
	with open(f, 'r') as handle:
		parsed = json.load(handle)

	for i in parsed['topartists']['artist']:
		print(i['name'])
