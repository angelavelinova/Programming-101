import unittest
from simplify_fraction import *
class TestReversedPolishNotation(unittest.TestCase):
	'''
	def test_validate_fraction_object_is_a_tuple(self):
		#self.assertRaises(ValidationError,simplify_fraction,[1,2])
		with self.assertRaises(ValidationError) as exc:
			simplify_fraction([1,2])
		self.assertEqual('', exc.exception)
		'''
	def test_when_nominator_equals_to_the_dominator_then_return_one_one(self):
		tuple = (5,5)
		expected_result = (1,1)
		self.assertEqual(simplify_fraction(tuple), expected_result)


	def test_when_denominator_percent_dominator_equals_to_zero_then_return_one_denominator_percent_dominator(self):
		tuple = (3,9)
		expected_result = (1,3)
		self.assertEqual(simplify_fraction(tuple), expected_result)

	def test_when_denominator_and_nominator_are_not_fr(self):
		tuple = (1,7)
		expected_result = (1,7)
		self.assertEqual(simplify_fraction(tuple), expected_result)

	def test_when_denominator_and_nominator_have_common_delim(self):
		tuple = (4,10)
		expected_result = (2,5)
		self.assertEqual(simplify_fraction(tuple), expected_result)

	def test_when_denominator_and_nominator_have_common_delim(self):
		tuple = (63,462)
		expected_result = (3,22)
		self.assertEqual(simplify_fraction(tuple), expected_result)

	def test_when_denominator_is_zero_then_return_tuple_of_zeroes(self):
		tuple = (63,0)
		expected_result = (0,0)
		self.assertEqual(simplify_fraction(tuple), expected_result)


	def test_collect_fractions(self):
		arg = [(1, 4), (1, 2)]
		expected_result = (3, 4)
		self.assertEqual(collect_fractions(arg), expected_result)

		arg = [(1, 7), (2, 6)]
		expected_result = (10, 21)
		self.assertEqual(collect_fractions(arg), expected_result)

	def test_sort_fractions(self):
		arg = [(2, 3), (1, 2)]
		expected_result = [(1, 2), (2, 3)]
		self.assertEqual(sort_fractions(arg), expected_result)

		arg = [(2, 3), (1, 2), (1, 3)]
		expected_result = [(1, 3), (1, 2), (2, 3)]
		self.assertEqual(sort_fractions(arg), expected_result)


if __name__ == '__main__':
	unittest.main()
