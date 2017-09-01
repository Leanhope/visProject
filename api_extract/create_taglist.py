#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import glob
import pathlib

source = '/home/hans/visProject/api_extract/artistTopTags/*.json'
token = 'ba3772fe9087004cadb3715a2f170555'
#url = 'http://ws.audioscrobbler.com/2.0/?method=artist.gettoptags'
tagset = set()

for f in glob.glob(source):
	print(f)
	with open(f, 'r') as handle:
		parsed = json.load(handle)
	try:
		for i in parsed['toptags']['tag']:
			tagset.add(i['name'])
	except KeyError as e:
		continue

text_file = open('tagset.txt', "w")
text_file.write(str(tagset))
text_file.close()
