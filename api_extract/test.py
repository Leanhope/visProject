import urllib.request, json
from collections import namedtuple
import requests
import glob, os
country = "Bangladesh;Belgium;Burkina Faso;Bulgaria;Bosnia and Herzegovina;Brunei Darussalam;Bolivia;Japan;Burundi;Benin;Bhutan;Jamaica;Botswana;Brazil;Bahamas;Belarus;Belize;Russian Federation;Rwanda;Serbia;Timor-Leste;Turkmenistan;Tajikistan;Romania;Guinea;Guatemala;Greece;Equatorial Guinea;Guyana;Georgia;United Kingdom;Gabon;Guinea;Gambia;Greenland;Ghana;Oman;Tunisia;Jordan;Croatia;Haiti;Hungary;Honduras;Puerto Rico;Palestine;Portugal;Paraguay;Panama;Papua New Guinea;Peru;Pakistan;Philippines;Poland;Zambia;Western Sahara;Estonia;Egypt;South Africa;Ecuador;Italy;Vietnam;Solomon Islands;Ethiopia;Somalia;Zimbabwe;Spain;Eritrea;Montenegro;Moldova;Madagascar;Morocco;Uzbekistan;Myanmar;Mali;Mongolia;Macedonia;Malawi;Mauritania;Uganda;Malaysia;Mexico;Israel;France;Somaliland;Finland;Fiji;Falkland Is.;Nicaragua;Netherlands;Norway;Namibia;Vanuatu;New Caledonia;Niger;Nigeria;New Zealand;Nepal;Kosovo;Cote d'Ivoire;Switzerland;Colombia;China;Cameroon;Chile;Cyprus;Canada;Congo;Central African Republic;Dem. Rep. Congo;Czech Republic;Cyprus;Costa Rica;Cuba;Swaziland;Syrian Arab Republic;Kyrgyzstan;Kenya;South Sudan;Suriname;Cambodia;El Salvador;Slovakia;Korea;Slovenia;Dem. Rep. Korea;Kuwait;Senegal;Sierra Leone;Kazakhstan;Saudi Arabia;Sweden;Sudan;Dominican Republic;Djibouti;Denmark;Germany;Yemen;Algeria;United States;Uruguay;Lebanon;Lao People's Democratic Republic;Taiwan;Trinidad and Tobago;Turkey;Sri Lanka;Latvia;Lithuania;Luxembourg;Liberia;Lesotho;Thailand;French Southern Territories;Togo;Chad;Libya;United Arab Emirates;Venezuela;Afghanistan;Iraq;Iceland;Iran;Armenia;Albania;Angola;Argentina;Australia;Austria;India;Tanzania;Azerbaijan;Ireland;Indonesia;Ukraine;Qatar;Mozambique"
#country = 'Bangladesh;Bosnia and Herz.'
limit = '200'
token = 'ba3772fe9087004cadb3715a2f170555'
url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks' #geoArtists
#url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettoptracks' #geoTracks

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
		text_file = open('geoTopTracks_200/'+c+'.json', "w")
		text_file.write(r.text)
		text_file.close()

error_file.close()