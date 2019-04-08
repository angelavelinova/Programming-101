import json
import random

def read_json():
	with open('cars.json','r') as f:
		information = json.load(f)
	return information

class Car:
	def __init__(self, car, model, max_speed):
		self.car = car
		self.model = model
		self.max_speed = max_speed

	def __str__(self):
		return "{}, {}, {}".format(self.car,self.model, self.max_speed)


class Driver:
	def __init__(self, name, car):
		self.name = name
		self.car = car

	def __str__(self):
		return "{}, {}".format(self.name,self.car)

class Race:
	def __init__(self, drivers, crash_chance):
		self.drivers = drivers
		self.crash_chance = crash_chance

	def __str__(self):
		return "{}, {}".format(self.drivers,self.crash_chance)

	def result(self):
		pass

class Championship:
	def __init__(self, name, races_count):
		self.name = name
		self.races_count = races_count

	def __str__(self):
		return "{}, {}".format(self.name,self.races_count)

	def top3(self):
		pass


information = read_json()
result = []
i = 0
while i < len(information['people']):
	curr_result = []
	curr_result.append(information['people'][i]['name'])
	curr_result.append(information['people'][i]['max_speed'])
	curr_result.append(0)
	curr_result.append(random.uniform(0, 1))
	curr_result.append(information['people'][i]['car'])
	curr_result.append(information['people'][i]['model'])
	result.append(curr_result)
	i += 1
result.sort(key=lambda x: x[1])
lenny = 0
Drivers = []
Cars = []
Races = []
Championships = []
while lenny < len(result):
	car = Car(result[lenny][4], result[lenny][5],result[lenny][1])
	Cars.append(car)
	driver = Driver(result[lenny][0],car)
	Drivers.append(driver)
	race = Race(driver,result[lenny][3])
	Races.append(race)
	championship = Championship(driver.name, result[lenny][2])
	Championships.append(championship)
	lenny += 1

rice = 3

crashed=""
j = 0
print("Starting a new championship called pandarace with",rice," races.")
print("Running ",rice," races ...")
while j < rice:
	print("Race #",j+1)
	print("###### START ######")
	ind =  len(result) - 1
	count = 0
	while count < 5:
		if Races[ind].crash_chance < 0.8 and Races[ind].crash_chance > 0:
			Championships[ind].races_count += (8 - count)
			count += 2
			ind -= 1
		elif Races[ind].crash_chance >= 0.8 and Races[ind].crash_chance <= 1:
			crashed+="Unfortunately, "+Drivers[ind].name+" has crashed."
			Races[ind].crash_chance = -1
			ind -= 1
		else:
			ind -= 1
	result.sort(key=lambda x: x[2])

	for i in range(0,3):
		if Races[len(result)-1-i].crash_chance != -1:
			print(Drivers[len(result)-1-i].name,Championships[len(result)-1-i].races_count)
		i += 1
	j += 1
	print(crashed)
