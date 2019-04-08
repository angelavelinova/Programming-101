from aggregated_money_tracker import *
from parse_money_tracker_data import *
from money_tracker import *

class MoneyTrackerMenu:
	def __init__(self, option):
		self.option = option
	
	aggregated_object = Aggregated_object()
	m = MoneyTracker(aggregated_object)

	def __init__(self, option):
		self.option = option

	def __str__(self):
		return "{} {}".format(self.option)

	def __repr__(self):
		return str(self.option, self.data)

	def __eq__(self, other):
		return self.option == other.option and self.data == other.data

	def solution(self, option):
		if option == 1:
			return m.all_data()
		if option == 2:
			date = sys.stdin.readline()
			return m.takes_by_date('=== ' + date + ' ===')
		if option == 3:
			return m.expenses_ordered_by_categories()
		if option == 4:
			amount = sys.stdin.readline()
			typee = sys.stdin.readline()
			date = sys.stdin.readline()
			return m.add_income(amount, typee, date)
		if option == 5:
			amount = sys.stdin.readline()
			typee = sys.stdin.readline()
			date = sys.stdin.readline()
			return m.add_expense(amount, typee, date)
		if option == 6:
			return


mu = MoneyTrackerMenu(1)
print(mu.solution(1))
