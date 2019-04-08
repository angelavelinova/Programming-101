import unittest
from coding_skills import *
filename="data.json"
class TestReversedPolishNotation(unittest.TestCase):

	def test_if_element_exist_in_dictionary(self):
		d = {"a":1, "b":2}
		expected_result = ['Mary Powell,gray,Wright-Hoover,dglover@yahoo.com,02870375047,4550\n']
		self.assertEqual(exist_element(1,d),True)

	def test_if_element_does_not_exist_in_dictionary(self):
		d = {"a":1, "b":2}
		expected_result = ['Mary Powell,gray,Wright-Hoover,dglover@yahoo.com,02870375047,4550\n']
		self.assertEqual(exist_element(5,d),False)

	def test_when_resurns_all_languages_and_people_with_max_score_for_each_of_them(self):
		expected_result = ['C++ - Cherna Ninja', 'PHP - Rado Rado', 'Python - Ivo Ivo', 'C# - Pavli Pavli', 'Haskell - Rado Rado', 'Java - Rado Rado', 'JavaScript - Rosi Rosi', 'Ruby - Rosi Rosi', 'CSS - Pavli Pavli', 'C - Cherna Ninja']
		self.assertEqual(coding_skill(filename),expected_result)





if __name__ == '__main__':
	unittest.main()
