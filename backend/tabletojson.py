

#Input: State Name, State Table file
#Output: State JSON with all counties as keys


#Relate the column names to the positions in the table, name is usually at 0
texas_map = {
	"cases" : 1,
	"deaths" : 2,
	"population" : 3
}


#Relate all the state names to their table maps
states_map = {
	"texas" : texas_map
}

table = open("texas.table")

json_out = "{\n"

for line in table:
	#Clean the line of the tab-separated table
	line = line.replace("\n", "")
	line = line.replace(",","")
	columns = line.split("\t")

	#Write to the json file
	json_out = json_out + ("\t\"" + columns[0] +"\" : {\n")
	for k,v in texas_map.items():
		json_out = json_out + ("\t\t\"" + k + "\" : " + columns[v] + ",\n")
	json_out = json_out[0:-2] + "\n"
	json_out = json_out + ("\t\t},\n")

json_out = json_out[0:-2] + "\n"
json_out = json_out + "}"

texas_json = open("texas.json","w")
texas_json.write(json_out)
print(json_out)