from pathlib import Path

#Input: State Name, State Table file
#Output: State JSON with all counties as keys


#Redone to always use the same columns since getstatetables.py is consistent with output
#Relate the column names to the positions in the table, name is usually at 0
state_map = {
	"cases" : 1,
	"deaths" : 2,
	"population" : 3
}


#Redone to always use the same columns since getstatetables.py is consistent with output
#Relate all the state names to their table maps
states_map = {
	"state" : state_map
}



def createJSON(path):
	table = open(path)

	line_count = 0
	

	json_out = "{\n"

	for line in table:
		line_count += 1

		#Clean the line of the tab-separated table
		line = line.replace("\n", "")
		line = line.replace(",","")
		columns = line.split("\t")

		#Write to the json file
		json_out = json_out + ("\t\"" + columns[0] +"\" : {\n")
		for k,v in state_map.items():
			val = columns[v]

			if(len(val) > 0 and val[0] not in "0123456789"): #if it is not a number
				val = "\"NaN\""
			else:
				val = val.split(" ")[0].split("(")[0]
			json_out = json_out + ("\t\t\"" + k + "\" : " + val + ",\n")
		json_out = json_out[0:-2] + "\n"
		json_out = json_out + ("\t\t},\n")



	json_out = json_out[0:-2] + "\n"
	json_out = json_out + "}"

	if(line_count == 0):
		print("*******NO LINES: " + path)
		return

	state_json = open("jsons/"+path.split("/")[1].split(".")[0]+".json","w")
	state_json.write(json_out)
	#print(json_out)

entries = Path('tables/')
for entry in entries.iterdir():
	if ".table" in entry.name:
		print(entry.name)
		createJSON("tables/" + entry.name)
