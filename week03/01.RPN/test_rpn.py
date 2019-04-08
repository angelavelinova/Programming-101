import unittest
from rpn_calculate import *
class TestReversedPolishNotation(unittest.TestCase):
	
	def test_when_single_digit_is_passed_then_return_the_same_digit(self):
		expr = '45'
		expected_result = '45.0'
		self.assertEqual(rpn_calculate(expr),expected_result)
	
	def test_when_two_numbers_are_pased_then_return_sum_of_them(self):
		expr = '4 8 +'
		expected_result = '12.0'
		self.assertEqual(rpn_calculate(expr),expected_result)

	def test_when_two_substraction_of_teo_numbers_then_return_their_difference(self):
		expr = '7 3 -'
		expected_result = '4.0'
		self.assertEqual(rpn_calculate(expr),expected_result)
	

	def test_if_is_deleted_two_elements_from_array(self):
		array = [1,2,3,4]
		position_to_delete = 2
		expected_array = [1,4]
		self.assertEqual(delete_two_positions(array, position_to_delete), expected_array)

	def test_if_is_deleted_element_from_array(self):
		array = [1,2,3,4]
		position_to_delete = 2
		expected_array = [1,2,4]
		self.assertEqual(delete_element(array, position_to_delete), expected_array)

	def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
		expr = '4 8 +'
		expected_result = '12.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
		expr = '5 4 + 1 +'
		expected_result = '10.0'
		self.assertEqual(rpn_calculate(expr), expected_result)
		
	def test_when_two_numbers_are_passed_then_return_substract_of_them(self):
		expr = '5 4 - 1 -'
		expected_result = '0.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_two_numbers_are_passed_then_return_delition_of_them(self):
		expr = '10 2 /'
		expected_result = '5.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_two_numbers_are_passed_then_return_multiplition_of_them(self):
		expr = '10 2 *'
		expected_result = '20.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_two_numbers_are_passed_then_return_first_on_pow_second(self):
		expr = '10 2 ^'
		expected_result = '100.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_two_numbers_are_passed_then_return_first_on_pow_second(self):
		expr = '100 sqrt'
		expected_result = '10.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_n_numbers_are_passed_then_return_max_of_them(self):
		expr = '1 2 3 4 5 8 7 max'
		expected_result = '8.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

	def test_when_n_numbers_are_passed_then_return_min_of_them(self):
		expr = '1 2 3 4 0 5 8 7 min'
		expected_result = '0.0'
		self.assertEqual(rpn_calculate(expr), expected_result)

if __name__ == '__main__':
	unittest.main()
