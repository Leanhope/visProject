#coding: utf8
import urllib
import json
from collections import namedtuple
import requests
import os.path

f = open('country_extract.json', 'r')
data = f.read()

w = open('countries.js', 'w')

final = "var countries = {\n"

data = json.loads(data)
error = 0

for i in data:
	code = i["Code"]
	name = i["Name"]
	
	final += "\""+code+"\": \""+name+"\",\n"
	
	
final += "}"

w.write(final)
w.close()