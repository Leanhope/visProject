import json
import os

counter = 0
source = '/home/hans/visProject/api_extract/geoTopArtists/'
for root, dirs, filenames in os.walk(source):
    for f in filenames:
		counter += 1
		print(f)
		print(counter)
		with open(f, 'r') as handle:
		    parsed = json.load(handle)

		for i in parsed['topartists']['artist']:
			print(i['name'])
