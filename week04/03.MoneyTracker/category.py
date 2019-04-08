class Category:
	def __init__(self, date, money):
		#self.category = category
		self.date = date
		self.money = money

	def __str__(self):
		return "{} {}".format(self.date, self.money)

	def __repr__(self):
		return str(self.date, self.money)

	def __eq__(self, other):
		print("muuuuu")
		return self.date == other.date and self.money == other.money
'''
mu = Category("20-01-2019", 20)
mu1 = Category("20-01-2019", 2)
print(mu,mu1)
print(mu==mu1)
print(str(mu))
'''
class Income(Category):
	def __init__(self, date, money, category):
		super().__init__(date, money)
		self.category = category

	def __str__(self):
		return super().__str__() +  " {}".format(self.category)

	def __repr__(self):
		return super().__repr__() + str(self.category)

	def __eq__(self, other):
		return self.date == other.date and self.money == other.money and self.category == other.category
		
class Expense(Category):
	def __init__(self, date, money, category):
		super().__init__(date, money)
		self.category = category

	def __str__(self):
		return super().__str__() +  " {}".format(self.category)

	def __repr__(self):
		return super().__repr__() + str(self.category)

	def __eq__(self, other):
		return self.date == other.date and self.money == other.money and self.category == other.category

'''
si = Income("20-01-2019", 20, "income")
si2 = Income("20-01-2019", 20, "income")
print(si,si2)
print(si==si2)
'''
