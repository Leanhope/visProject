import json
import os
import glob
from collections import defaultdict

source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'

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
		#print(name)
		with open(src, 'r') as handler:
			parsed2 = json.load(handler)
			try:
				for j in range(7):
					items.append(parsed2['toptags']['tag'][j]['name'])
					#print(parsed2['toptags']['tag'][j]['name'])
			except KeyError as e:
				continue
			except IndexError as k:
				continue

	for i in items:
		counts[i] +=  1 #counts.get(i, 0) + 1

	sort = sorted(counts, key=counts.get, reverse=True)

	for w in range(500):
		try:
			#pass
			final[sort[w]] = counts[sort[w]]
			#final.update({sort[w] : counts[sort[w]]})
		except IndexError as e:
			continue

		#print(sort[w], counts[sort[w]])
	
	#print(final)
	summ = 0
	for i in final:
		summ += final[i]
	
	d = []

	for w in range(500):
		try:
			final_perc[sort[w]] = counts[sort[w]]/summ
			temp_dict = dict()
			temp_dict["tags"] = final_perc
			collection["name: " + file] = temp_dict
			tag = {sort[w]:counts[sort[w]]/summ*100}
			
			#tag = str(sort[w]) + "\"" + ":" +  "\"" + str(counts[sort[w]]/summ*100)
			#print(tag)
			#print(tag)			
			d.append(tag)# = {"name":f, "tags":[{"tag":final_perc[sort[w]], "size":counts[sort[w]]/summ}]}
			#a.append(d)
			#final.update({sort[w] : counts[sort[w]]})
		except IndexError as e:
			continue
	tag = {"name":file, "tags":d}
	#tag = {file:d}
	a.append(tag)


collection_head["countries"] = collection
countries = {"toptags":a}
#print(countries)
with open('results.json', 'w') as fp:
	json.dump(countries, fp)
#f = open('results.json', 'w')
#f.write(j)
#f.close()
#print(final_perc)
#print(sorted(counts, key=counts.get()))