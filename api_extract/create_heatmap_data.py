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
final = str()
tag =  sys.argv[1]
with open('country_extract.json', 'r') as handle:
	parsed = json.load(handle)

	with open('results.json', 'r') as results:
		parsed_results = json.load(results)

		for i in parsed_results["toptags"]:

			for j in parsed["Countries"]:
				if j["Name"].lower() == i["name"].lower():
					code = j["Code"]

			total = 0		
			
			try:
				for x in i["tags"]:
					if tag in str(list(x.keys())).replace("'", "").replace("[","").replace("]",""): 
						
						value = (str(list(x.values())).replace("[","").replace("]",""))
						total += float(value)
				final += ("\""+code+"\""+ ": " +  str(total)+","+"\n")			
			except Exception as e:
				print(e)

final = str("var "+tag+" = {" + "\n" + str(final) + "};")
text_file = open("../tags/" + tag + '.js', "w")
text_file.write(final)
text_file.close()
