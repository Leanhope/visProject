import json
import os
import glob
from collections import defaultdict

source = '/home/hans/visProject/api_extract/geoTopArtists/*.json'
	
for f in glob.glob(source):
	items = list()
	counts = defaultdict(int)
	final = dict()
	final_perc = dict()
	print(f)
	with open(f, 'r') as handle:
		parsed = json.load(handle)

	for i in parsed['topartists']['artist']:
		name = i['name'].replace("/", "")
		src = "/home/hans/visProject/api_extract/artistTopTags/"+name+".json"
		#print(name)
		with open(src, 'r') as handler:
			parsed2 = json.load(handler)
			try:
				for j in range(5):
					items.append(parsed2['toptags']['tag'][j]['name'])
					#print(parsed2['toptags']['tag'][j]['name'])
			except KeyError as e:
				continue
			except IndexError as k:
				continue

	for i in items:
		counts[i] +=  1 #counts.get(i, 0) + 1

	sort = sorted(counts, key=counts.get, reverse=True)

	for w in range(15):
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
	
	for w in range(15):
		try:
			final_perc[sort[w]] = counts[sort[w]]/summ
			#final.update({sort[w] : counts[sort[w]]})
		except IndexError as e:
			continue
	print(final_perc)
	#print(sorted(counts, key=counts.get()))