import urllib.request
from bs4 import BeautifulSoup
from statistics import mode

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
	"Lousiana",
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


def outputFromState(state):
	print("--------")
	print(state)
	
	url = state.replace(" ", "_")
	url = "https://en.wikipedia.org/wiki/COVID-19_pandemic_in_" + url
	wiki = urllib.request.urlopen(url)

	wiki_file = open("tables/"+state + ".table","w")
	output = ""

	soup = BeautifulSoup(wiki, "lxml")
	right_table = soup.find('table', class_='wikitable')
	if right_table is None:
		print("THIS STATE NO TABLE FOUND" + state)
		return

	print(right_table)

	rows = right_table.findAll('tr')

	row_lens = [len(row.findAll("td")) for row in rows]
	data_length = mode(row_lens)

	
	print(data_length)

	name_i = 0
	cases_i = 0
	deaths_i = 0
	pop_i = 0

	col_headers = rows[0].findAll("th")

	for i in range(len(col_headers)):
		text = (col_headers[i].find(text=True)).lower()
		#print(i, col_headers[i].find(text=True))
		#-1 is for the fact that county is always #1 and is not included
		#in the list later
		if "cases" == text:
			cases_i = i - 1
		elif "deaths" in text:
			deaths_i = i - 1
		elif "pop" in text:
			pop_i = i - 1



	
	print("cases i ",cases_i)
	print("deaths i ", deaths_i)
	print("pop i ",pop_i)


	

	for row in rows:
		#print(row)
		county = {
			"name" : "undefined",
			"cases" : "-1",
			"deaths" : "-1",
			"population" : "-1"

		}
		cells = row.findAll("td")
		if len(cells) == data_length:
			#print(cells)
			county["name"] = str(row.findAll("th")[0].find(text=True).replace("\n","").replace(",",""))
			county["cases"] = str(cells[cases_i].find(text=True).replace("\n","").replace(",",""))
			county["deaths"] = str(cells[deaths_i].find(text=True).replace("\n","").replace(",",""))
			county["population"] = str(cells[pop_i].find(text=True).replace("\n","").replace(",",""))

			output = output + str(county["name"]) + "\t"
			output = output + str(county["cases"]) + "\t"
			output = output + str(county["deaths"]) + "\t"
			output = output + str(county["population"]) + "\n"
			#print(county, cells[0].find(text=True), cells[1].find(text=True), cells[2].find(text=True))

	wiki_file.write(output)

for state in states[states.index("Georgia"):]:
	outputFromState(state)