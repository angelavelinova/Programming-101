import unittest
from aggregated_money_tracker import *
class TestAggregatedObject(unittest.TestCase):

	def test_when_returns_dictionary_from_array_with_data_rows_from_input_text_file(self):
		aggregated_object = Aggregated_object()
		a = aggregated_object.aggregate_object()
		self.assertIsInstance(a, dict)

	def test_if_data_from_dictionary_is_correct(self):
		aggregated_object = Aggregated_object()
		a = aggregated_object.aggregate_object()
		expected_result = {'=== 22-03-2019 ===': ['760, Salary, New Income', '5.5, Eating Out, New Expense', '34, Clothes, New Expense', '41.79, Food, New Expense', '12, Eating Out, New Expense', '7, House, New Expense', '14, Pets, New Expense', '112.40, Bills, New Expense', '21.5, Transport, New Expense', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense'], '=== 23-03-2019 ===': ['50, Savings, New Income', '15, Food, New Expense', '200, Deposit, New Income', '5, Sports, New Expense', '10, Food, 22-04-2019'], '=== 22-12-2019 ===': ['20, mau,  New Expense'], '=== 7-04-2019 ===': ['20, mom,  New Income'], '=== 1-1-2019 ===': ['40, Clothes,  New Expense ']}

		self.assertEqual(a, expected_result)
		

if __name__ == '__main__':
	unittest.main()
