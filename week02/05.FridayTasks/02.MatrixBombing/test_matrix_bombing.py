import unittest
from week2_friday1 import *
class TestMatrixBombing(unittest.TestCase):
	def test_matrix_bombing(self):
		m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		expected_result = {(0, 0): 42, (0, 1): 36, (0, 2): 37, (1, 0): 30, (1, 1): 15, (1, 2): 23, (2, 0): 29, (2, 1): 15, (2, 2): 26}
		self.assertEqual(matrix_bombing_plan(m),expected_result)



	
if __name__ == '__main__':
	unittest.main()
