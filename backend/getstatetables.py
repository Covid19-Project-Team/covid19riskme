import urllib.request
from bs4 import BeautifulSoup

wiki = urllib.request.urlopen("https://en.wikipedia.org/wiki/COVID-19_pandemic_in_Texas")

wiki_file = open("texas.table","w")
output = ""

soup = BeautifulSoup(wiki, "lxml")
right_table = soup.find('table', class_='wikitable')
#print(right_table)

for row in right_table.findAll('tr'):
	#print(row)
	cells = row.findAll("td")
	if len(cells) == 3:
		county = row.findAll("th")[0].find(text=True)
		
		output = output + str(county.replace("\n","").replace(",","")) + "\t"
		output = output + str(cells[0].find(text=True).replace("\n","").replace(",","")) + "\t"
		output = output + str(cells[1].find(text=True).replace("\n","").replace(",","")) + "\t"
		output = output + str(cells[2].find(text=True).replace("\n","").replace(",","")) + "\n"
		#print(county, cells[0].find(text=True), cells[1].find(text=True), cells[2].find(text=True))

wiki_file.write(output)