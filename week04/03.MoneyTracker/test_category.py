import unittest
from category import *
class TestAggregatedObject(unittest.TestCase):

	def test_when_returns_category_object(self):
		a = Category("20-01-2019", 20)
		self.assertIsInstance(a, Category)

	def test_when_checks_if_two_category_objects_are_equal(self):
		a = Category("20-01-2019", 20)
		b = Category("20-01-2019", 2)
		self.assertEqual(a==b, False)

	def test_when_prints_object(self):
		a = Category("20-01-2019", 20)
		self.assertEqual(str(a),"20-01-2019 20")

	def test_when_returns_income_object(self):
		a = Income("20-01-2019", 20, "income")
		self.assertIsInstance(a, Income)

	def test_when_checks_if_two_income_objects_are_equal(self):
		a = Income("20-01-2019", 20, "income")
		b = Income("20-01-2019", 25, "income")
		self.assertEqual(a==b, False)

	def test_when_prints_income_object(self):
		a = Income("20-01-2019", 20, "income")
		print(a)
		self.assertEqual(str(a),"20-01-2019 20 income")

	def test_when_returns_expense_object(self):
		a = Expense("20-01-2019", 20, "expense")
		self.assertIsInstance(a, Expense)

	def test_when_checks_if_two_expense_objects_are_equal(self):
		a = Expense("20-01-2019", 20, "expense")
		b = Expense("20-01-2019", 25, "expense")
		self.assertEqual(a==b, False)

	def test_when_prints_expense_object(self):
		a = Expense("20-01-2019", 20, "expense")
		self.assertEqual(str(a),"20-01-2019 20 expense")



if __name__ == '__main__':
	unittest.main()
