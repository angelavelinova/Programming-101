import unittest
from money_tracker_menu import *
class TestMoneyTrackerMenu(unittest.TestCase):

	def test_when_returns_money_tracker_object(self):
		aggregated_object = Aggregated_object()
		m = MoneyTracker(aggregated_object)
		self.assertIsInstance(m, MoneyTracker)

	def test_when_prints_all_data(self):
		m = MoneyTrackerMenu(1)
		self.assertEqual(m.solution(1),{'=== 22-03-2019 ===': ['760, Salary, New Income', '5.5, Eating Out, New Expense', '34, Clothes, New Expense', '41.79, Food, New Expense', '12, Eating Out, New Expense', '7, House, New Expense', '14, Pets, New Expense', '112.40, Bills, New Expense', '21.5, Transport, New Expense', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income'], '=== 23-03-2019 ===': ['50, Savings, New Income', '15, Food, New Expense', '200, Deposit, New Income', '5, Sports, New Expense', '10, Food, 22-04-2019'], '=== 22-12-2019 ===': ['20, mau,  New Expense'], '=== 7-04-2019 ===': ['20, mom,  New Income'], '=== 1-1-2019 ===': ['40, Clothes,  New Expense ']})

if __name__ == '__main__':
	unittest.main()
