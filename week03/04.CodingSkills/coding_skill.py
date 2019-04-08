
import json
import sys
#filename = 'data.json'

def exist_element(element,dict):
	for key in dict.keys():
		if element == dict[key]:
			return True
	return False

def coding_skill(filename):
	with open(filename, 'r') as f:
		data = json.load(f)

	people = data['people']
	people_array = []
	language_dict= {}
	i = 0
	while i < len(people):
		j= 0
		people_array.append(people[i]['first_name']+" " +people[i]['last_name'])
		while j < len(people[i]['skills']):
			if not exist_element(people[i]['skills'][j]['name'], language_dict):
				language_dict[people[i]['skills'][j]['name']] = [0,""]
			j += 1
		i += 1
	lang_ind = 0
	result = []
	while lang_ind < len(language_dict):
		max_count = 0
		person = ""
		people_ind = 0
		while people_ind < len(people):
			skill_ind = 0
			while skill_ind < len(people[people_ind]['skills']):
				if language_dict[people[people_ind]['skills'][skill_ind]['name']][0] < int(people[people_ind]['skills'][skill_ind]['level']):
					language_dict[people[people_ind]['skills'][skill_ind]['name']][0] = int(people[people_ind]['skills'][skill_ind]['level'])
					language_dict[people[people_ind]['skills'][skill_ind]['name']][1] = people_array[people_ind]
				skill_ind += 1
			people_ind += 1
		lang_ind += 1

	for key in language_dict.keys():
		result.append(key + " - " + language_dict[key][1])
	return result

def main():
	arguments = sys.argv
	print(coding_skill(arguments[1]))

if __name__ == '__main__':
	main()
