import shutil
from category import *
from aggregated_money_tracker import *
from parse_money_tracker_data import *
filename = "money_tracker.txt"

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
	
def delete_file(filename):
	with open(filename, "w") as myfile:
		myfile.write("")

class MoneyTracker:

	def __init__(self, aggregated_object):
		self.aggregated_object = Aggregated_object()
		self.aggregated_object = aggregated_object.aggregate_object()

	def all_data(self):
		return self.aggregated_object

	def takes_by_date(self,date):
		result = []
		for key in self.aggregated_object:
			if key == date:
				for value in self.aggregated_object[key]:
					result.append(value)

		return result

	def takes_incomes(self):
		result = []
		for key in self.aggregated_object:
			for i in range(0, len(self.aggregated_object[key])):
				if substr("New Income", self.aggregated_object[key][i]):
					result.append(self.aggregated_object[key][i])

		return result

	def takes_expenses(self):
		result = []
		for key in self.aggregated_object:
			for i in range(0, len(self.aggregated_object[key])):
				if substr("New Expense", self.aggregated_object[key][i]):
					result.append(self.aggregated_object[key][i])

		return result

	def add_income(self, amount, typee, date):
		self.aggregated_object['=== '+date+' ==='].append(str(amount)+', '+ typee+ ", New Income")
		delete_file(filename)
		for key in self.aggregated_object:
			with open(filename, "a+") as myfile:
				myfile.write('\n'+key)
			for i in range(0, len(self.aggregated_object[key])): 
				with open(filename, "a+") as myfile:
					myfile.write('\n'+self.aggregated_object[key][i])

		source_file = open(filename, 'r')
		source_file.readline()
		target_file = open(filename, 'w')
		shutil.copyfileobj(source_file, target_file)


	def add_expense(self, amount, typee, date):
		self.aggregated_object['=== '+date+' ==='].append(str(amount)+', '+ typee+ ", New Expense")
		delete_file(filename)
		for key in self.aggregated_object:
			with open(filename, "a+") as myfile:
				myfile.write('\n'+key)
			for i in range(0, len(self.aggregated_object[key])): 
				with open(filename, "a+") as myfile:
					myfile.write('\n'+self.aggregated_object[key][i])

		source_file = open(filename, 'r')
		source_file.readline()
		target_file = open(filename, 'w')
		shutil.copyfileobj(source_file, target_file)

	def expenses_ordered_by_categories(self):
		result = []
		pass

		return result

'''
aggregated_object = Aggregated_object()
m = MoneyTracker(aggregated_object)
a = m.all_data()
#print(a)
a1 = m.takes_by_date("=== 22-03-2019 ===")
#print(a1)
a2 = m.takes_incomes()
#print(a2)
a3 = m.takes_expenses()
#print(a3)
m.add_income(20,"food",'22-03-2019')
#a4 = m.all_data()
m.add_expense(50,"food",'22-03-2019')
'''
