import unittest
from parse_money_tracker_data import *
class TestParseFunction(unittest.TestCase):

	def test_when_opens_valid_text_file_and_returns_object_from_type_data(self):
		fname = "money_tracker.txt"
		rows = Data(fname)
		self.assertIsInstance(rows, Data)

	def test_when_parses_data_from_valid_text_file(self):
		fname = "money_tracker.txt"
		rows = Data(fname)
		rows = rows.data()
		expected_result = ['=== 22-03-2019 ===', '760, Salary, New Income',
		 '5.5, Eating Out, New Expense', '34, Clothes, New Expense', '41.79, Food, New Expense', 
		 '12, Eating Out, New Expense', '7, House, New Expense', '14, Pets, New Expense', 
		 '112.40, Bills, New Expense', '21.5, Transport, New Expense', '20, food, New Income', 
		 '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', 
		 '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income',
		  '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '=== 23-03-2019 ===',
		   '50, Savings, New Income', '15, Food, New Expense', '200, Deposit, New Income', '5, Sports, New Expense', 
		   '10, Food, 22-04-2019', '=== 22-12-2019 ===', '20, mau,  New Expense', '=== 7-04-2019 ===',
			'20, mom,  New Income', '=== 1-1-2019 ===', '40, Clothes,  New Expense ']

		self.assertEqual(rows, expected_result)
		

if __name__ == '__main__':
	unittest.main()
