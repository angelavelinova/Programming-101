class Bill:

	def __init__(self, amount):
		self.amount = amount

	def validate(self):
		if self.amount < 0:
			raise ValueError('amount should not be less than 0!')
		if not isinstance(self.amount, int):
			raise TypeError('amount should be int!')

	def __str__(self):
		self.validate()
		return 'A {}$ amount'.format(self.amount)

	def __repr__(self):
		return '{}'.format(self.amount)
		#return self.__str__()

	def __int__(self):
		self.validate()
		return int(self.amount)

	def __eq__(self, other):
		return self.amount == other.amount

	def __hash__(self):
		return hash(self.amount)

a = Bill(10)
print(a)
print(str(a))
print(int(a))
b = Bill(5)
c = Bill(10)
print(a == b)
print(a == c)

money_holder = {}

money_holder[a] = 1 # We have one 10% bill

if c in money_holder:
	money_holder[c] += 1

print(money_holder) # { "A 10$ bill": 2 }


class BatchBill:
	def validate(self):
		if not isinstance(self.lst, list):
			raise TypeError('lst should be list!')

	def __init__(self, lst):
		self.lst = lst

	def __len__(self):
		return len(self.lst)

	def total(self):
		total_amount = 0
		i = 0
		while i < len(self.lst):
			total_amount += int(self.lst[i])
			i += 1
		return total_amount

	def __getitem__(self, index):
		return self.lst[index]

listy = BatchBill([1,2,3,4,5])
print(len(listy))
print(listy.total())

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]
print(bills)
batch = BatchBill(bills)

for bill in batch:
	print(bill)


class CashDesk:
	total_money=0
	bills=[]

	def __init__(self):
		pass

	def take_money(self,money):
		if isinstance(money,Bill):
			self.total_money += money.amount
			self.bills.append(money)
		if isinstance(money,BatchBill):
			self.total_money += money.total()
			for bill in money:
				self.bills.append(bill)
			
	def total(self):
		return self.total_money

	def inspect(self):
		print("We have the following count of bills, sorted in ascending order:")
		unique_bills=[]
		for bill in self.bills:
			if bill not in unique_bills:
				unique_bills.append(bill)
		for bill in unique_bills:
			s=str(int(bill))+'$ bills '+str(self.bills.count(bill))
			print(s)


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)
print(batch)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))
print(desk)
print(desk.total()) # 390
desk.inspect()
