import json
import os
import glob

source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'
	
for f in glob.glob(source):
	print(f)
