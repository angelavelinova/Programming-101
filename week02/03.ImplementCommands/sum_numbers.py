import sys

def sum_numbers(filename):
	f = open(filename,'r')
	string_numbers = f.readlines()[0]
	string_numbers+=" "
	i = 0
	sum_numbers = 0
	current_number = ""
	while i < len(string_numbers):
		if string_numbers[i] >= "0" and string_numbers[i] <= "9":
			current_number += string_numbers[i]
		elif string_numbers[i] == " ":
			current_number = int(current_number)
			sum_numbers += current_number
			current_number = ""
		elif string_numbers[i] == "":
			current_number = int(current_number)
			sum_numbers += current_number
			break
		i += 1

	f.close()
	return sum_numbers


def main():
	arguments = sys.argv
	print(sum_numbers(arguments[1]))
	

if __name__ == '__main__':
	main()
