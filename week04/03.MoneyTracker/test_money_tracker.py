import unittest
from money_tracker import *
class TestMoneyTracker(unittest.TestCase):

	def test_when_returns_True_if_string_is_substring_on_other_srting(self):
		s1 = "aba"
		s2 = "babababa"
		self.assertEqual(substr(s1,s2), True)

	def test_when_returns_False_if_string_is_not_substring_on_other_srting(self):
		s1 = "aba"
		s2 = "babababa"
		self.assertEqual(substr(s2,s1), False)

	def test_when_returns_True_if_string_is_substring_on_itself(self):
		s1 = "aba"
		self.assertEqual(substr(s1,s1), True)

	def setUp(self):
		aggregated_object = Aggregated_object()
		self.m = MoneyTracker(aggregated_object)

	def test_if_new_object_if_is_from_type_MoneyTracker(self):
		self.assertIsInstance(self.m, MoneyTracker)

	def test_when_returns_all_data(self):
		a = self.m.all_data()
		expected_result = {'=== 22-03-2019 ===': ['760, Salary, New Income', '5.5, Eating Out, New Expense', '34, Clothes, New Expense', '41.79, Food, New Expense', '12, Eating Out, New Expense', '7, House, New Expense', '14, Pets, New Expense', '112.40, Bills, New Expense', '21.5, Transport, New Expense', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense'], '=== 23-03-2019 ===': ['50, Savings, New Income', '15, Food, New Expense', '200, Deposit, New Income', '5, Sports, New Expense', '10, Food, 22-04-2019'], '=== 22-12-2019 ===': ['20, mau,  New Expense'], '=== 7-04-2019 ===': ['20, mom,  New Income'], '=== 1-1-2019 ===': ['40, Clothes,  New Expense ']}
		self.assertEqual(a, expected_result)

	def test_when_returns_array_of_data_by_date(self):
		a = self.m.takes_by_date("=== 22-03-2019 ===")
		expected_result = ['760, Salary, New Income', '5.5, Eating Out, New Expense', '34, Clothes, New Expense', '41.79, Food, New Expense', '12, Eating Out, New Expense', '7, House, New Expense', '14, Pets, New Expense', '112.40, Bills, New Expense', '21.5, Transport, New Expense', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense', '20, food, New Income', '50, food, New Expense']
		self.assertEqual(a, expected_result)
		
	def test_when_returns_array_of_data_with_all_incomes(self):
		a = self.m.takes_incomes()
		expected_result = ['760, Salary, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '50, Savings, New Income', '200, Deposit, New Income', '20, mom,  New Income']
		self.assertEqual(a, expected_result)

	def test_when_returns_array_of_data_with_all_expenses(self):
		a = self.m.takes_expenses()
		expected_result = ['5.5, Eating Out, New Expense', '34, Clothes, New Expense', '41.79, Food, New Expense', '12, Eating Out, New Expense', '7, House, New Expense', '14, Pets, New Expense', '112.40, Bills, New Expense', '21.5, Transport, New Expense', '50, food, New Expense', '50, food, New Expense', '50, food, New Expense', '50, food, New Expense', '15, Food, New Expense', '5, Sports, New Expense', '20, mau,  New Expense', '40, Clothes,  New Expense ']
		self.assertEqual(a, expected_result)

	def test_when_adds_income_and_returns_array_of_data_with_all_incomes(self):
		a = self.m.add_income(20,"food",'22-03-2019')
		expected_result = ['760, Salary, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '20, food, New Income', '50, Savings, New Income', '200, Deposit, New Income', '20, mom,  New Income','20, mom,  New Income']
		self.assertEqual(a, expected_result)


if __name__ == '__main__':
	unittest.main()
