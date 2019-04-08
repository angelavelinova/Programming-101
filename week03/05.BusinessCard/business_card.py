import json
import sys
def delete_new_line(string):
	string=string[0:len(string)-1]
	return string

def substr(substring, string):
	i = 0
	j = 0
	flag = False
	while j < len(string) and i < len(substring):
		if substring[i]!=string[j]:
			i = 0
			j += 1
		else:
			i += 1
			j += 1
		if i == len(substring):
			flag = True
	
	return flag

def delete_word(row):
	i = 0
	ind = 0
	while i < len(row):
		if row[i] == ":":
			ind = i 
		i += 1
	res = ""
	for j in range(ind+1, len(row)):
		if ord(row[j]) != 34:
			res += row[j]
	i = 0
	res1 = ""
	while i < len(res):
		if res[i] != " ":
			res1+=res[i]
		i += 1
	return res1

def read_file(arguments, name):
	f = open(arguments,'r')
	i = 0
	array = f.readlines()
	length = len(array)
	data_name = []
	while i < length-1:
		if substr(name, array[i]):
			while array[i] != '        }]\n':
				data_name.append(delete_word(array[i]))
				i += 1
		i+=1
	return data_name
	f.close()


def write_into_html(data, name):
	filename = name + '.html'
	f = open(filename,'w')
	i = 0
	skills = data[8:len(data)]
	interests = data[6]
	interests = interests[1:len(interests)-3]
	inter = interests.split(',')
	f.write('<!DOCTYPE html>' + '\n')
	f.write('\t' + '<html>' + '\n')
	f.write('\t'+'\t' + '<head>' + '\n')
	f.write('\t'+'\t' + '\t' + '<title>' + data[0][0:len(data[0])-2] + '</title>' + '\n')
	f.write('\t'+'\t' + '\t' + '<link rel="stylesheet" type="text/css" href="styles.css">' + '\n')
	f.write('\t'+'\t' + '</head>' + '\n')
	f.write('\t'+'\t' + '<body>' + '\n')
	f.write('\t'+'\t' + '\t' + '<div class="business-card male">' + '\n')
	f.write('\t'+'\t' + '\t' + '<h1 class="full-name">' + data[0][0:len(data[0])-2] + '\t' + data[1][0:len(data[1])-2] + '</h1>'+'\n')
	f.write('\t'+'\t' + '\t' + '<img class="avatar" src="avatars/"' + data[7][0:len(data[7])-2]+ '"> <div class="base-info">' + '\n')
	f.write('\t'+'\t' + '\t' + '<div class="base-info">' + '\n')
	f.write('\t'+'\t' + '\t' + '<p>Age: ' + data[2][0:len(data[2])-2] + '</p>'+ '\n')
	f.write('\t'+'\t' + '\t' + '<p>Birth date: ' + data[3][0:len(data[3])-2] + '</p>'+ '\n')
	f.write('\t'+'\t' + '\t' + '<p>Birth place: ' + data[4][0:len(data[4])-2] + '</p>'+ '\n')
	f.write('\t'+'\t' + '\t' + '<p>Gender: ' + data[5][0:len(data[5])-2] + '</p>'+ '\n')
	f.write('\t'+'\t' + '\t' + '</div>' +'\n')
	f.write('\t'+'\t' + '\t' + '<div class="interests">'+'\n')
	f.write('\t'+'\t' + '\t' + '<h2>Interests:</h2>'+'\n')
	f.write('\t'+'\t' + '\t' + "<ul>"+ '\n')
	int_ind = 0
	while int_ind < len(inter):
		f.write('\t'+'\t' + '\t' + '<li>' + inter[int_ind] + ' </li>' +'\n')
		int_ind += 1
	f.write('\t'+'\t' + '\t' + '</ul>' +'\n')
	f.write('\t'+'\t' + '\t' + '</div>' +'\n')
	f.write('\t'+'\t' + '\t' + '<div class="skills">' +'\n')
	f.write('\t'+'\t' + '\t' + '<h2>Skills:</h2>' + '\n')
	f.write('\t'+'\t' + '\t' + '<ul>' + '\n')
	sk = 1
	while sk < len(skills)-1:
		if skills[sk]  !=  '},{ '  and skills[sk] != '[{':
			f.write('\t'+'\t' + '\t' +'<li>' + skills[sk][0:len(skills[sk])-2] + ' - ' +skills[sk+1][0:len(skills[sk+1])-1] +  '</li>' +'\n')
		sk += 3

	f.write('\n' + '\t'+'\t' + '\t' +'</ul>' +'\n')
	f.write('\t'+'\t' + '\t' +'</div>' +'\n')
	f.write('\t'+'\t' + '\t' +'</div>' +'\n')
	f.write('\t'+'\t' +'</body>' +'\n')
	f.write('\t'+'</html>' +'\n')
	f.close()
	return filename

def main():
	result = []
	data = read_file("business_card_data.json","Ivo")
	result.append(write_into_html(data, "rado_rado"))

	data = read_file("business_card_data.json","Rado")
	result.append(write_into_html(data, "rado_rado"))

	data = read_file("business_card_data.json","Rosi")
	result.append(write_into_html(data, "rosi_rosi"))

	data = read_file("business_card_data.json","Pavli")
	result.append(write_into_html(data, "pavli_pavli"))

	data = read_file("business_card_data.json","Cherna")
	result.append(write_into_html(data, "cherna_nindja"))

	print(result)

if __name__ == '__main__':
	main()
