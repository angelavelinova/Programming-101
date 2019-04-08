import sys
#Show all user data(incomes and expenses).
def data(filename):
	f = open(filename,'r')
	i = 0
	array = f.readlines()
	f.close()
	return array

def delete_new_line(string):
	string=string[0:len(string)-1]
	return string

def list_user_data(all_user_data):
	return data(all_user_data)



def show_user_incomes(all_user_data):
	result = []
	i = 0
	array = data(all_user_data)
	length = len(array)
	while i < length-1:
		if substr("New Income", array[i]):
			result.append(delete_new_line(array[i]))
		i+=1
	print(result)
	return result


def show_user_savings(all_user_data):
	f = open(all_user_data,'r')
	i = 0
	array = f.readlines()
	length = len(array)
	while i < length-1:
		if substr("Savings", array[i]):
			print(delete_new_line(array[i]))
		i+=1
	f.close()


def show_user_deposits(all_user_data):
	f = open(all_user_data,'r')
	i = 0
	array = f.readlines()
	length = len(array)
	while i < length-1:
		if substr("Deposit", array[i]):
			print(delete_new_line(array[i]))
		i+=1
	#print(array[i])
	f.close()

#Lists all expense categories
def show_user_expenses(all_user_data):
	f = open(all_user_data,'r')
	i = 0
	array = f.readlines()
	length = len(array)
	while i < length-1:
		if substr("New Expense", array[i]):
			print(delete_new_line(array[i]))
		i+=1
	f.close()


def list_user_expenses_ordered_by_categories(all_user_data):
	pass

#Show user data for specific date.
def show_user_data_per_date(date, all_user_data):
	i = 0
	array = data(all_user_data)
	result = []
	length = len(array)
	while i < length:
		if array[i] == '=== '+date+' ==='+'\n':
			result.append(delete_new_line(array[i]))
			i += 1
			while i < length and array[i][0] != '=':
				result.append(delete_new_line(array[i]))
				i += 1
		i+=1
	return result


def exist_in(element,array):
	i = 0
	while i < len(array):
		if array[i] == element:
			return True
		i += 1
	return False

def delete_duplicates(array):
	result = []#["" for col in range(len(array))]
	i = 0
	#result_ind = 0
	while i < len(array):
		if not exist_in(array[i], result) and array[i] != "":
			result.append(array[i])
		i += 1
	return result

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

def list_income_categories(all_user_data):
	result = []
	i = 0
	array = data(all_user_data)
	length = len(array)
	categories = ["" for col in range(length)]
	ind_categories = 0
	while i < length:
		if array[i][0] != '=':
			j = 0
			while j < len(array[i]):
				while array[i][j] != ',':
					j += 1
				j += 1
				while array[i][j] !=',':
					categories[ind_categories]+=array[i][j]
					j += 1
				j =  len(array[i])
			ind_categories += 1
		i += 1
	categories_without_duplicates = delete_duplicates(categories)
	ind = 0
	while ind < len(categories_without_duplicates):
		i = 0
		while i < len(array):
			if substr(categories_without_duplicates[ind],array[i]) and substr("New Income",array[i]):
				result.append(array[i])
			i += 1
		ind += 1		
	return result

#show expenses, ordered by categories
def list_expense_categories(all_user_data):
	result = []
	i = 0
	array = data(all_user_data)
	length = len(array)
	categories = ["" for col in range(length)]
	ind_categories = 0
	while i < length:
		if array[i][0] != '=':
			j = 0
			while j < len(array[i]):
				while array[i][j] != ',':
					j += 1
				j += 1
				while array[i][j] !=',':
					categories[ind_categories]+=array[i][j]
					j += 1
				j =  len(array[i])
			ind_categories += 1
		i += 1
	categories_without_duplicates = delete_duplicates(categories)
	ind = 0
	while ind < len(categories_without_duplicates):
		i = 0
		while i < len(array):
			if substr(categories_without_duplicates[ind],array[i]) and substr("New Expense",array[i]):
				result.append(array[i])
			i += 1
		ind += 1
	print(result)		
	return result


#The user can add new income or expense for specific date and category.
def add_income(income_category, money, date, all_user_data):
	money = delete_new_line(money)
	income_category = delete_new_line(income_category)
	date = delete_new_line(date)
	new_data = "\n=== " + date +" ===\n" + money + ", " + income_category + ", " +" New Income "
	with open(all_user_data, "a+") as myfile:
		myfile.write(str(new_data))
	all_user_data+='\n'+new_data+'\n'
	return all_user_data


def add_expense(expense_category, money, date, all_user_data):
	money = delete_new_line(money)
	expense_category = delete_new_line(expense_category)
	date = delete_new_line(date)
	new_data = "\n=== " + date +" ===\n" + money + ", " + expense_category + ", " +" New Expense "
	with open(all_user_data, "a+") as myfile:
		myfile.write(str(new_data))
	all_user_data+='\n'+new_data+'\n'
	return all_user_data

def main():

	filename = "money_tracker.txt"
	print("Hi! Choose one of the following options to continue:\n","1 - show all data\n",
		"2 - show data for specific date\n","3 - show expenses, ordered by categories\n",
		"4 - add new income\n","5 - add new expense\n","6 - exit\n")
	option = sys.stdin.readline()
	option =  delete_new_line(option)

	if option == '1':#show all data
		array = list_user_data(filename)
		length = len(array)
		i = 0
		while i < length-1:
			print(delete_new_line(array[i]))
			i+=1
		print(array[i])

		
	elif option == '2':#show data for specific date
		print("Select specific date:\n")
		date = sys.stdin.readline()
		date =  delete_new_line(date)
		array = show_user_data_per_date(date, filename)
		length = len(array)
		i = 0
		while i < length-1:
			print(array[i])
			i+=1
		
	elif option == '3':#show expenses, ordered by categories
		array = list_expense_categories(filename)
		length = len(array)
		i = 0
		while i < length-1:
			print(array[i])
			i+=1
	
	elif option == '4':#add new income
		print("New income amount:")
		money = sys.stdin.readline()
		print("New income type:")
		income_category = sys.stdin.readline()
		print("New income date:")
		date = sys.stdin.readline()
		array = data(filename)
		array = add_income(income_category, money, date, filename)
		
	elif option == '5':#add new expense
		print("New expense amount:")
		money = sys.stdin.readline()
		print("New expense type:")
		expense_category = sys.stdin.readline()
		print("New expense date:")
		date = sys.stdin.readline()
		array = data(filename)
		array = add_expense(expense_category, money, date, filename)

	if option == '6':#add new expense
		#print("exit")
		exit()
	
if __name__ == '__main__':
	main()
