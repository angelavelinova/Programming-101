import unittest
from cash_desk import *
class TestCashDesk(unittest.TestCase):
	def setUp(self):
		self.a = Bill(10)
		self.b = Bill(15)
		self.listy = BatchBill([1,2,3,4,5])

		self.values = [10, 20, 50, 100, 100, 100]
		self.bills = [Bill(value) for value in values]
		self.batch = BatchBill(bills)
		self.desk = CashDesk()

	def test_if_object_is_instance_of_class_bill(self):
		self.assertIsInstance(self.a, Bill)

	def test_when_prints_object_of_class_bill(self):
		res = str(self.a)
		self.assertEqual(res, "A 10$ amount")

	def test_when_prints_object_of_class_bill(self):
		res = str(self.a)
		self.assertEqual(res, "A 10$ amount")

	def test_when_prints_value_of_an_object_of_class_bill(self):
		self.assertEqual(int(self.a), 10)

	def test_when_checks_if_two_objects_of_class_bill_are_equal(self):
		self.assertEqual(self.a == self.a, True)
		self.assertEqual(self.a == self.b, False)

	def test_when_object_of_class_bill_is_hashed(self):
		self.assertEqual(hash(self.a), 10)

	def test_money_holder_dictionary_with_value_of_bill_as_a_key_and_number_of_bills_as_a_value(self):
		money_holder = {}
		money_holder[self.a] = 1 # We have one 10% bill
		if c in money_holder:
			money_holder[c] += 1
			
		self.assertEqual(str(money_holder), "{10: 2}")

	def test_if_object_is_instance_of_class_BatchBill(self):
		self.assertIsInstance(self.listy, BatchBill)

	def test_when_returns_length_of_an_object_of_class_BatchBill(self):
		self.assertEqual(len(self.listy), 5)

	def test_when_returns_total_count_of_list(self):
		self.assertEqual(self.listy.total(), 15)

	def test_if_object_is_instance_of_class_cashdesk(self):
		self.assertIsInstance(self.desk, CashDesk)

	def test_when_returns_taken_money(self):
		self.desk.take_money(self.batch)
		self.desk.take_money(Bill(10))
		self.assertIsInstance(self.desk, CashDesk)

	def test_when_returns_total_amount_of_money(self):
		self.desk.take_money(self.batch)
		self.desk.take_money(Bill(10))
		self.assertEqual(self.desk.total(), 190)

if __name__ == '__main__':
	unittest.main()
