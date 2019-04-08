import unittest
from AdditionalTasks import *
class TestAdditionalTasks(unittest.TestCase):
	def test_if_two_words_are_anagrams(self):
		word1 = "TOP_CODER"
		word2 = "COTO_PRODE"
		expected_result = "NOT ANAGRAMS"
		self.assertEqual(anagrams(word1, word2),expected_result)

		word1 = "boro"
		word2 = "kilata"
		expected_result = "NOT ANAGRAMS"
		self.assertEqual(anagrams(word1, word2),expected_result)

		word1 = "BRADE"
		word2 = "BEARD"
		expected_result = "ANAGRAMS"
		self.assertEqual(anagrams(word1, word2),expected_result)

	def test_returns_if_credit_card_is_valid(self):
		number = 79927398713
		expected_result = True
		self.assertEqual(is_credit_card_valid(number),expected_result)

		number = 79927398715
		expected_result = False
		self.assertEqual(is_credit_card_valid(number),expected_result)

	def test_returns_if_number_is_prime(self):
		n = 11
		expected_result = True
		self.assertEqual(is_prime(n),expected_result)

		n = 121
		expected_result = False
		self.assertEqual(is_prime(n),expected_result)

	def test_returns_if_element_exist_in_array(self):
		element = 2
		array = [1,2,3,4]
		expected_result = True
		self.assertEqual(exist_in(element,array),expected_result)

		element = 2
		array = [1,5,3,4]
		expected_result = False
		self.assertEqual(exist_in(element,array),expected_result)



	def test_returns_a_list_of_tuples_that_is_the_goldbach_conjecture_for_the_given_number_n(self):
		n = 4
		expected_result = [(2, 2)]
		self.assertEqual(goldbach(n),expected_result)

		n = 6
		expected_result = [(3, 3)]

		self.assertEqual(goldbach(n),expected_result)

		n = 8
		expected_result = [(3, 5)]
		self.assertEqual(goldbach(n),expected_result)

		n = 10
		expected_result = [(3, 7), (5, 5)]
		self.assertEqual(goldbach(n),expected_result)

		n = 100
		expected_result = [(3, 97), (11, 89), (17, 83), (29, 71), (41, 59), (47, 53)]
		self.assertEqual(goldbach(n),expected_result)


	
if __name__ == '__main__':
	unittest.main()
