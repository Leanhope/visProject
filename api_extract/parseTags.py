import json
import os
import glob
from collections import defaultdict

#This python file is designed to extract the top tags of every country  out of
#their respective TopArtists file and represent them in percentages.

source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'

#So many container for temporary data because json is confusing
collection = dict()
collection_head = dict()
a = []
superfinal = []

for f in glob.glob(source):
	items = list()
	counts = defaultdict(int)
	final = dict()
	final_perc = dict()
	file = (os.path.basename(f).replace(".json", ""))
	with open(f, 'r') as handle:
		parsed = json.load(handle)

	for i in parsed['topartists']['artist']:
		name = i['name'].replace("/", "")
		src = "/home/hans/visProject/api_extract/artistTopTags/"+name+".json"
		with open(src, 'r') as handler:
			parsed2 = json.load(handler)
			try:
				for j in range(7): #Amount of tags taken per artist
					items.append(parsed2['toptags']['tag'][j]['name'])
			except KeyError as e:
				continue
			except IndexError as k:
				continue

	for i in items:
		counts[i] +=  1 #increment if tag is found again

	sort = sorted(counts, key=counts.get, reverse=True) #sort decrementing

	for w in range(500):
		try:
			final[sort[w]] = counts[sort[w]] #assign the counts to the tags
		except IndexError as e:
			continue

	summ = 0
	for i in final:
		summ += final[i] #total count of tags for percentage calculation
	
	d = []

	for w in range(500):
		try:
			final_perc[sort[w]] = counts[sort[w]]/summ
			temp_dict = dict()
			temp_dict["tags"] = final_perc
			collection["name: " + file] = temp_dict
			tag = {sort[w]:counts[sort[w]]/summ*100}
					
			d.append(tag) #create new list containing the percentage counts

		except IndexError as e:
			continue
	tag = {"name":file, "tags":d} #bring together country names and tags
	a.append(tag)


collection_head["countries"] = collection
countries = {"toptags":a} #final json file. i dont like json

with open('results.json', 'w') as fp:
	json.dump(countries, fp)
