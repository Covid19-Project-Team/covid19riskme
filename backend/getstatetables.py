import urllib.request
from bs4 import BeautifulSoup
from statistics import mode

states_dict = {
    "Alabama" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Alabama",
    "Alaska" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Alaska",
    "Arizona" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Arizona",
    "Arkansas" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Arkansas",
    "California" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_California",
    "Colorado" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Colorado",
    "Connecticut" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Connecticut",
    "Delaware" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Delaware",
    "District of Columbia" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Washington,_D.C.",
    "Florida" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Florida",
    "Georgia" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Georgia_(U.S._state)",
    "Hawaii" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Hawaii",
    "Idaho" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Idaho",
    #"Illinois" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Illinois",
    "Indiana" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Indiana",
    "Iowa" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Iowa",
    "Kansas" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Kansas",
    "Kentucky" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Kentucky",
    "Lousiana" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Louisiana",
    "Maine" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Maine",
    #"Maryland" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Maryland",
    "Massachusetts" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Massachusetts",
    #"Michigan" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Michigan",
    "Minnesota" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Minnesota",
    "Mississippi" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Mississippi",
    "Missouri" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Missouri",
    "Montana" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Montana",
    "Nebraska" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nebraska",
    "Nevada" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Nevada",
    #"New Hampshire" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_New_Hampshire",
    "New Jersey" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_New_Jersey",
    "New Mexico" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_New_Mexico",
    #"New York" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_New_York_(state)",
    "North Carolina" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_North_Carolina",
    "North Dakota" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_North_Dakota",
    "Ohio" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Ohio",
    "Oklahoma" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Oklahoma",
    #"Oregon" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Oregon",
    "Pennsylvania" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Pennsylvania",
    "Puerto Rico" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Puerto_Rico",
    "Rhode Island" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Rhode_Island",
    "South Carolina" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Carolina",
    #"South Dakota" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_South_Dakota",
    #"Tennessee" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Tennessee",
    "Texas" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Texas",
    "the United States Virgin Islands" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States_Virgin_Islands",
    #"Utah" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Utah",
    "Vermont" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Vermont",
    "Virginia" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Virginia",
    "Washington" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Washington_(state)",
    "West Virginia" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_West_Virginia",
    "Wisconsin" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Wisconsin",
    "Wyoming" : "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Wyoming"
}


states = [
	"Alabama",
	"Alaska",
	"Arizona",
	"Arkansas",
	"California",
	"Colorado",
	"Connecticut",
	"Delaware",
	"Washington, D.C.",
	"Florida",
	"Georgia",
	"Hawaii",
	"Idaho",
	"Illinois",
	"Indiana",
	"Iowa",
	"Kansas",
	"Kentucky",
	"Louisiana",
	"Maine",
	"Maryland",
	"Massachusetts",
	"Michigan",
	"Minnesota",
	"Mississippi",
	"Missouri",
	"Montana",
	"Nebraska",
	"Nevada",
	"New Hampshire",
	"New Jersey",
	"New Mexico",
	"New York",
	"North Carolina",
	"North Dakota",
	"Ohio",
	"Oklahoma",
	"Oregon",
	"Pennsylvania",
	"Puerto Rico",
	"Rhode Island",
	"South Carolina",
	"South Dakota",
	"Tennessee",
	"Texas",
	"the United States Virgin Islands",
	"Utah",
	"Vermont",
	"Virginia",
	"Washington",
	"West Virginia",
	"Wisconsin",
	"Wyoming"
	]


def outputFromState(state, url):
	print("--------")
	print(state)
	
	#url = state.replace(" ", "_")
	#url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_" + url
	#print ("\t\""+state + "\" : \"" + url + "\", ")
	#return
	wiki = urllib.request.urlopen(url)

	wiki_file = open("tables/"+state + ".table","w")
	output = ""

	soup = BeautifulSoup(wiki, "lxml")
	right_table = soup.find('table', class_='wikitable')
	if right_table is None:
		print("THIS STATE NO TABLE FOUND" + state)
		return


	#print(right_table)

	rows = right_table.findAll('tr')

	row_lens = [len(row.findAll("td")) for row in rows]
	data_length = mode(row_lens)

	
	print(data_length)

	name_i = 0
	cases_i = 0
	deaths_i = 0
	pop_i = 0

	row_index = 0
	if(state == "Arkansas" or state == "Wisconsin"):
		row_index = 1

	col_headers = rows[row_index].findAll("th")

	#print(col_headers)
	#return

	for i in range(len(col_headers)):
		text = (col_headers[i].find(text=True)).lower()
		#print(i, col_headers[i].find(text=True))
		#-1 is for the fact that county is always #1 and is not included
		#in the list later
		#print(col_headers)
		print(text)
		if "cases" in text and cases_i == 0:
			cases_i = i
		elif (("deaths" in text) and deaths_i == 0 and (not ("/" in text)) and (not ("100" in text))) :
			deaths_i = i
		elif "pop" in text:
			pop_i = i

	cases_i -= 1 if cases_i > 0 else 0
	deaths_i -= 1 if deaths_i > 0 else 0
	pop_i -= 1 if pop_i > 0 else 0


	
	print("cases i ",cases_i )
	print("deaths i ", deaths_i if deaths_i != 0 else str(deaths_i) + " Maybe Wrong")
	print("pop i ",pop_i if pop_i != 0 else str(pop_i) + " Maybe Wrong")


	

	for row in rows:
		#print(row)
		county = {
			"name" : "undefined",
			"cases" : "\"NaN\"",
			"deaths" : "\"NaN\"",
			"population" : "\"NaN\""

		}
		cells = row.findAll("td")
		if len(cells) == data_length:
			#print(cells)
			countyth = row.findAll("th")
			countyth_idx = 0 if state != "Wisconsin" else 1 # wisconsin is special

			if countyth is None or len(countyth) == 0:
				print(state + " ERROR")
				print(countyth)
				print(row)
				return

			county["name"] = str(countyth[countyth_idx].find(text=True).replace("\n","").replace(",",""))
			county["cases"] = str(cells[cases_i].find(text=True).replace("\n","").replace(",",""))
			county["deaths"] = str(cells[deaths_i].find(text=True).replace("\n","").replace(",",""))
			county["population"] = str(cells[pop_i].find(text=True).replace("\n","").replace(",",""))

			output = output + str(county["name"]) + "\t"
			output = output + str(county["cases"]) + "\t"
			output = output + str(county["deaths"]) + "\t"
			output = output + str(county["population"]) + "\n"
			#print(county, cells[0].find(text=True), cells[1].find(text=True), cells[2].find(text=True))

	wiki_file.write(output)

#for state in states[states.index("Georgia"):]:
for state, url in states_dict.items():
	outputFromState(state, url)