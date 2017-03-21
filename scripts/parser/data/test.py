import json

DATA = []

with open('institutes.json', 'r') as file:
	DATA = json.load(file)

def print_data():
	for item in DATA:
		print(item)

def parse():
	with open('instituteinfo2.py', 'w') as target:
		target.write("institutes = [")
		counter = 0

		for item in DATA:
			acronym = item['pk'].split('-')[1]
			name = item['fields']['name']
			faculty = item['fields']['faculty']

			if counter == len(DATA) -1:
				target.write("{'new_acronym':" + "'" + acronym + "'," + "'new_name':" + "'" + name + "'," + "'new_faculty':" + "'" + faculty + "'" + '}' )
				target.write(']')
			
			else:
				target.write("{'new_acronym':" + "'" + acronym + "'," + "'new_name':" + "'" + name + "'," + "'new_faculty':" + "'" + faculty + "'" + '},' )
				counter += 1



parse()
