import urllib#.request
import json
from collections import namedtuple
import requests
import glob, os
country = 'Bangladesh;Belgium;Burkina Faso;Bulgaria;Bosnia and Herzegovina;Brunei Darussalam;Bolivia;Japan;Burundi;Benin;Bhutan;Jamaica;Botswana;Brazil;Bahamas;Belarus;Belize;Russian Federation;Rwanda;Serbia;Timor-Leste;Turkmenistan;Tajikistan;Romania;Guinea;Guatemala;Greece;Equatorial Guinea;Guyana;Georgia;United Kingdom;Gabon;Guinea;Gambia;Greenland;Ghana;Oman;Tunisia;Jordan;Croatia;Haiti;Hungary;Honduras;Puerto Pico;Palestine;Portugal;Paraguay;Panama;Papua New Guinea;Peru;Pakistan;Philippines;Poland;Zambia;Western Sahara;Estonia;Egypt;South Africa;Ecuador;Italy;Vietnam;Solomon Is.;Ethiopia;Somalia;Zimbabwe;Spain;Eritrea;Montenegro;Moldova;Madagascar;Morocco;Uzbekistan;Myanmar;Mali;Mongolia;Macedonia;Malawi;Mauritania;Uganda;Malaysia;Mexico;Israel;France;Somaliland;Finland;Fiji;Falkland Is.;Nicaragua;Netherlands;Norway;Namibia;Vanuatu;New Caledonia;Niger;Nigeria;New Zealand;Nepal;Kosovo;Cote de Ivoire;Switzerland;Colombia;China;Cameroon;Chile;N. Cyprus;Canada;Congo;Central African Rep.;Dem. Rep. Congo;Czech Rep.;Cyprus;Costa Rica;Cuba;Swaziland;Syria;Kyrgyzstan;Kenya;S. Sudan;Suriname;Cambodia;El Salvador;Slovakia;Korea;Slovenia;Dem. Rep. Korea;Kuwait;Senegal;Sierra Leone;Kazakhstan;Saudi Arabia;Sweden;Sudan;Dominican Rep.;Djibouti;Denmark;Germany;Yemen;Algeria;United States;Uruguay;Lebanon;Lao PDR;Taiwan;Trinidad and Tobago;Turkey;Sri Lanka;Latvia;Lithuania;Luxembourg;Liberia;Lesotho;Thailand;Fr. S. Antarctic Lands;Togo;Chad;Libya;United Arab Emirates;Venezuela;Afghanistan;Iraq;Iceland;Iran;Armenia;Albania;Angola;Argentina;Australia;Austria;India;Tanzania;Azerbaijan;Ireland;Indonesia;Ukraine;Qatar;Mozambiqueff'
#country = 'Bangladesh;Bosnia and Herz.'
limit = '200'
token = 'ba3772fe9087004cadb3715a2f170555'
#url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists' #geoArtists
url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks' #geoTracks


country = country.split(';')
error_file = open('geoTopArtists/_error.txt', "w")

for c in country:
	temp = url+'&country='+c+'&api_key='+token+'&format=json&limit='+limit
	r = requests.get(temp)
	print(c)	
	data = json.loads(r.text)

	if 'error' in data:
		error_file.write(c+"\n")
		print('error')
	else:	
		text_file = open('geoTopTracks/'+c+'.json', "w")
		text_file.write(r.text)
		text_file.close()

error_file.close()