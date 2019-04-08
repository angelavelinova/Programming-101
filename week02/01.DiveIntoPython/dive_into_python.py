#1.Gas Stations
def gas_stations(distance, tank_size, stations):
	stations.append(distance)
	stations[:0-1]
	path = []
	new_tank_size = tank_size
	last_station = stations[0]
	station_index = 0
	while station_index <len(stations):
		distance_between_stations = stations[station_index] - last_station
		if new_tank_size <= distance_between_stations:
			path.append(last_station)
			last_station = stations[station_index]
		else:
			last_station = stations[station_index]
			new_tank_size -= distance_between_stations
		new_tank_size = tank_size - distance_between_stations
		station_index += 1
	return path

#2.Is Number Balanced
def is_number_balanced(number):
	string_number=str(number)
	length_number = len(string_number)
	left_sum = 0
	right_sum = 0
	if length_number == 1:
		return True
	middle = length_number//2
	for i in range(0, middle):
		left_sum += int(string_number[i])
		right_sum += int(string_number[length_number - i - 1])
	return left_sum == right_sum

#3.Increasing and Decreasing Sequences
def increasing_or_decreasing(seq):
	dec_flag = True
	for i in range (0,len(seq)-1):
		if seq[i] - 1 != seq[i+1]:
			dec_flag = False
	inc_flag = True
	for i in range (0,len(seq)-1):
		if seq[i] + 1 != seq[i+1]:
			inc_flag = False
	if(dec_flag):
		return "Down!"
	if(inc_flag):
		return "Up!"
	return False

#4.Largest Palindrome
def palindrome(n):
	n=str(n)
	copy_n = n
	len_n = len(n)
	i = 0
	is_palindrome = True
	middle = len_n//2
	while i < middle:
		if(n[i]!=n[len_n-i-1]):
			is_palindrome=False
		i = i+1
	return is_palindrome
def get_largest_palindrome(n):
	res = n
	found_result = False
	while found_result == False and res > 0:
		res -= 1
		if palindrome(res):
			found_result = True
	return res


#5.Sum all numbers in a given string
def sum_of_numbers(input_string):
	sum_of_numbers = 0
	current_number = ""
	for i in range(0,len(input_string)):
		if ord(input_string[i]) >= 48 and ord(input_string[i]) <= 57:
			current_number += input_string[i]
		else:
			if current_number !="":
				sum_of_numbers += int(current_number)
			current_number=""
	if(current_number.isdigit()):
		sum_of_numbers += int(current_number)

	return sum_of_numbers

#6.Birthday Ranges
def in_range(number,start,end):
	return number >= start and number <= end
def birthday_ranges(birthdays, ranges):
	len_birthdays = len(birthdays)
	len_ranges = len(ranges)
	result = [0 for i in range(len_ranges)]
	for i in range(0, len_birthdays):
		for j in range(0, len_ranges):
			if in_range(birthdays[i], ranges[j][0],ranges[j][1]):
				result[j] += 1



	return result

#7.100 SMS
def to_string(array):
	res = ""
	for i in range(0,len(array)):
		res += str(array[i])
	return res

def numbers_to_message(pressed_sequence):
	dict = {'1':"1",
			'2':"a",'22':"b",'222':"c",
			'3':"d",'33':"e",'333':"f",
			'4':"g",'44':"h",'444':"i",
			'5':"j",'55':"k",'555':"l",
			'6':"m",'66':"n",'666':"o",
			'7':"p",'77':"q",'777':"r",'7777':"s",
			'8':"t",'88':"u",'888':"v",
			'9':"w",'99':"x",'999':"y","9999":'z',
			'0': " ",
			'-1': "",
			'-':""
		 }
	result=""
	pressed_sequence= to_string(pressed_sequence)
	i = 0
	flag = True
	upper = False
	symbol = ""
	count = 0 
	while(flag and i < len(pressed_sequence)):
		if i == 0:
			symbol = pressed_sequence[i]
			if symbol =='-' and pressed_sequence[i+1]=='1':
				symbol = ""
				i += 3
			elif symbol != pressed_sequence[i+1]:
				if symbol=='1':
					upper = True

				if symbol!='1':
					if(len(symbol)<4):
						if upper == True:
							result+=dict[symbol].upper()
							upper=False
					elif(len(symbol)%4==0 and (symbol[0]!='7' and symbol[0]!='9')):
						symbol=symbol[0]
						result+=dict[symbol]
					elif(len(symbol)%4==1 and (symbol[0]!='7' and symbol[0]!='9')):
						symbol=symbol[0]+symbol[1]
						result+=dict[symbol]
					elif(len(symbol)%4==2 and (symbol[0]!='7' and symbol[0]!='9')):
						symbol=symbol[0]+symbol[1]+symbol[2]
						result+=dict[symbol]
					elif(len(symbol)%5==0  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]
						result+=dict[symbol]
					elif(len(symbol)%5==1  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]+symbol[1]
						result+=dict[symbol]
					elif(len(symbol)%5==2  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]+symbol[1]+symbol[2]
						result+=dict[symbol]
					elif(len(symbol)%5==3  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]+symbol[1]+symbol[2]+symbol[3]
						result+=dict[symbol]


				symbol = pressed_sequence[i+1]
				i += 1
			else:
				symbol += pressed_sequence[i]
				i += 1

		elif i > 0 and i < len(pressed_sequence)-1:
			if pressed_sequence[i] != pressed_sequence[i+1]:
				if symbol!='1':
					if(len(symbol)<4 and symbol[0]!='7' and symbol[0]!='9'):
						result+=dict[symbol]

					elif(len(symbol)<5 and (symbol[0]=='7' or symbol[0]=='9')):
						result+=dict[symbol]

					elif(len(symbol)%4==0 and (symbol[0]!='7' and symbol[0]!='9')):
						symbol=symbol[0]
						result+=dict[symbol]
					elif(len(symbol)%4==1 and (symbol[0]!='7' and symbol[0]!='9')):
						symbol=symbol[0]+symbol[1]
						result+=dict[symbol]
					elif(len(symbol)%4==2 and (symbol[0]!='7' and symbol[0]!='9')):
						symbol=symbol[0]+symbol[1]+symbol[2]
						result+=dict[symbol]

					elif(len(symbol)%5==0 and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]
						result+=dict[symbol]
					elif(len(symbol)%5==1  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]+symbol[1]
						result+=dict[symbol]
					elif(len(symbol)%5==2  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]+symbol[1]+symbol[2]
						result+=dict[symbol]
					elif(len(symbol)%5==3  and (symbol[0]=='7' or symbol[0]=='9')):
						symbol=symbol[0]+symbol[1]+symbol[2]+symbol[3]
						result+=dict[symbol]
				symbol = pressed_sequence[i+1]
				i += 1
			else:
				symbol += pressed_sequence[i+1]
				i += 1
		else:
			if symbol!='1':
				if(len(symbol)<4 and symbol[0]!='7' and symbol[0]!='9'):
					result+=dict[symbol]

				elif(len(symbol)<5 and (symbol[0]=='7' or symbol[0]=='9')):
					result+=dict[symbol]

				elif(len(symbol)%4==0 and (symbol[0]!='7' and symbol[0]!='9')):
					symbol=symbol[0]
					result+=dict[symbol]
				elif(len(symbol)%4==1 and (symbol[0]!='7' and symbol[0]!='9')):
					symbol=symbol[0]+symbol[1]
					result+=dict[symbol]
				elif(len(symbol)%4==2 and (symbol[0]!='7' and symbol[0]!='9')):
					symbol=symbol[0]+symbol[1]+symbol[2]
					result+=dict[symbol]

				elif(len(symbol)%5==0 and (symbol[0]=='7' or symbol[0]=='9')):
					symbol=symbol[0]
					result+=dict[symbol]
				elif(len(symbol)%5==1  and (symbol[0]=='7' or symbol[0]=='9')):
					symbol=symbol[0]+symbol[1]
					result+=dict[symbol]
				elif(len(symbol)%5==2  and (symbol[0]=='7' or symbol[0]=='9')):
					symbol=symbol[0]+symbol[1]+symbol[2]
					result+=dict[symbol]
				elif(len(symbol)%5==3  and (symbol[0]=='7' or symbol[0]=='9')):
					symbol=symbol[0]+symbol[1]+symbol[2]+symbol[3]
					result+=dict[symbol]
			flag = False


	return result

def message_to_numbers(message):
	dict = {'^':"1",
			'a':"2",'b':"22",'c':"222",
			'd':"3",'e':"33",'f':"333",
			'g':"4",'h':"44",'i':"444",
			'j':"5",'k':"55",'l':"555",
			'm':"6",'n':"66",'o':"666",
			'p':"7",'q':"77",'r':"777",'s':"7777",
			't':"8",'u':"88",'v':"888",
			'w':"9",'x':"99",'y':'999',"z":'9999',
			' ':'0'
		 }
	result=""
	index = 0
	current_symbol = ""
	i = 0
	while i <= len(message):
		if i == len(message):
			list_array = []
			for j in range(0, len(result)):
				if result[j] != ';' and result[j] != ':':
					list_array.append(int(result[j]))
				elif result[j] == ';':
					list_array.append(-1)
			return list_array
		if message[i] >= 'A' and message[i] <='Z':
			result+=str(1)

		current_symbol = dict[message[i].lower()]
		#print(current_symbol[0],'\n',"res",result,"res")
		if  result!="" and current_symbol[0] == result[len(result)-2]:
			result+=';'
		result+=current_symbol+':'
		i += 1
		
		

def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    if people_weight == [] or people_floors == []:
        return 0
    trips = 0
    current_weight = 0
    start = 0
    for index, person_weight in enumerate(people_weight):
        current_weight += person_weight
        if current_weight > max_weight or len(people_weight[start:index]) >= max_people:
            trips += len(set(people_floors[start:index])) + 1
            current_weight = person_weight
            start = index
    trips += len(set(people_floors[start:]))+1
    return trips
