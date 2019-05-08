import unittest
from Generators import *

class TestGenerators(unittest.TestCase):
	def test_when_returns_concatenation_of_two_iterables(self):
		a = range(0,4)
		b = range(4, 8)
		expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
		self.assertEqual(list(chain(a, b)), expected_result)

		a = {0, 1, 2, 3}
		b = {4, 5, 6, 7}
		expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
		self.assertEqual(list(chain(a, b)).sort(), expected_result.sort())

	def test_when_returns_concatenation_of_iterable_and_list(self):
		a = range(0,4)
		b = [4,5,6,7]
		expected_result = [0, 1, 2, 3, 4, 5, 6, 7]
		self.assertEqual(list(chain(a, b)), expected_result)

	def test_when_returns_iterable_which_has_true_on_same_position_in_mask_array(self):
		iterables = ["Ivo", "Rado", "Panda"]
		mask = [False, False, True]
		expected_result = ["Panda"]
		self.assertEqual(list(compress(iterables, mask)), expected_result)


if __name__ == '__main__':
	unittest.main()
