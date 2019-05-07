import unittest
from polynomial import *
class TestPolynomial(unittest.TestCase):
	def setUp(self):
		self.t = Term(coeff=4, variable='x', power=3)
		self.p = Term(coeff=5, variable='x', power=3)
		self.c = Term(coeff=5, variable=None, power=0)

	def test_when_returns_true_when_number_is_integer_and_false_if_is_not(self):
		self.assertEqual(is_int(5), True)
		self.assertEqual(is_int("a"), False)

	def test_when_returns_tuple_with_variable_and_its_power_by_string(self):
		self.assertEqual(variable_and_power("x^5"), ('x',5))
		self.assertEqual(variable_and_power("x"), ('x',1))

	def test_when_returns_tuple_with_coefficient_variable_and_its_power_by_string(self):
		self.assertEqual(term("4*x^5"), (4,'x',5))
		self.assertEqual(term("x"), (1,'x',1))

	def test_when_returns_coefficient_by_string(self):
		self.assertEqual(coefficient("4*x^5"), 4)
		self.assertEqual(coefficient("x^5"), 1)

	def test_when_object_is_from_class_Term(self):
		self.assertIsInstance(self.t, Term)

	def test_when_add_two_objects_from_class_Term(self):
		self.assertEqual(str(self.t+self.p), "9*x^3")

	def test_when_checks_if_two_objects_from_class_Term_are_equal(self):
		self.assertEqual(self.t==self.t, True)
		self.assertEqual(self.t==self.p, False)
	
	def test_when_returns_object_from_class_Term(self):
		self.assertEqual(str(self.t), "4*x^3")

	def test_when_parse_tuple_from_string(self):
		self.assertEqual(self.t.parse_from_string("4*x^3"),(4,'x',3))

	def test_when_parse_tuple_from_string_only_with_constant(self):
		self.assertEqual(self.t.constant(4),(4,None,0))

	def test_if_returns_true_when_argument_is_constant(self):
		self.assertEqual(self.c.is_constant,True)

	def test_when_returns_derivative_of_a_string(self):
		self.assertEqual(str(self.t.derivative()),"12*x^2")

if __name__ == '__main__':
	unittest.main()
