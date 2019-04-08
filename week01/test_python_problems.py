import unittest
from problems_week1 import *
class TestProblemsFromWeek01(unittest.TestCase):
	def test_when_returns_sum_of_all_digits_of_number(self):
		number = 1325132435356
		expected_result = 43
		self.assertEqual(sum_of_digits(number),expected_result)

		number = 123
		expected_result = 6
		self.assertEqual(sum_of_digits(number),expected_result)

		number = 6
		expected_result = 6
		self.assertEqual(sum_of_digits(number),expected_result)

		number = -10
		expected_result = 1
		self.assertEqual(sum_of_digits(number),expected_result)

	def test_when_returns_length_of_all_digits_of_number(self):
		number = 10000
		expected_result = 5
		self.assertEqual(len_digits(number),expected_result)

	def test_when_returns_length_of_all_digits_of_number(self):
		number = 10000
		expected_result = 5
		self.assertEqual(len_digits(number),expected_result)

	def test_when_returns_list_of_digits_from_number(self):
		n = 123
		expected_result = [1,2,3]
		self.assertEqual(to_digits(n),expected_result)

		n = 99999
		expected_result = [9, 9, 9, 9, 9]
		self.assertEqual(to_digits(n),expected_result)

		n = 123023
		expected_result = [1, 2, 3, 0, 2, 3]
		self.assertEqual(to_digits(n),expected_result)

	def test_when_returns_number_from_list_of_digits(self):
		lst = [1,2,3]
		expected_result = 123
		self.assertEqual(to_number(lst),expected_result)

		lst = [1,2,3]
		expected_result = 123
		self.assertEqual(to_number(lst),expected_result)

		lst = [9,9,9,9,9]
		expected_result = 99999
		self.assertEqual(to_number(lst),expected_result)

		lst = [1,2,3,0,2,3]
		expected_result = 123023
		self.assertEqual(to_number(lst),expected_result)

		lst = [21, 2, 33]
		expected_result = 21233
		self.assertEqual(to_number(lst),expected_result)

	def test_when_returns_factorial_of_a_number(self):
		n = 5
		expected_result = 120
		self.assertEqual(fact(n),expected_result)

	def test_when_returns_the_sum_of_the_factorials_of_each_digit_of_a_number(self):
		n = 111
		expected_result = 3
		self.assertEqual(fact_digits(n),expected_result)

		n = 145
		expected_result = 145
		self.assertEqual(fact_digits(n),expected_result)

		n = 999
		expected_result = 1088640
		self.assertEqual(fact_digits(n),expected_result)

	def test_if_objects_string_representation_is_a_palindrome(self):
		n = 121
		expected_result = True
		self.assertEqual(palindrome(n),expected_result)

		n = "kapak"
		expected_result = True
		self.assertEqual(palindrome(n),expected_result)

		n = "baba"
		expected_result = False
		self.assertEqual(palindrome(n),expected_result)

	def test_if_returns_the_count_of_all_vowels_in_the_string(self):
		string = "Python"
		expected_result = 2
		self.assertEqual(count_vowels(string),expected_result)

		string = "Theistareykjarbunga"
		expected_result = 8
		self.assertEqual(count_vowels(string),expected_result)

		string = "grrrrgh!"
		expected_result = 0
		self.assertEqual(count_vowels(string),expected_result)

		string = "Github is the second best thing that happend to programmers, after the keyboard!"
		expected_result = 22
		self.assertEqual(count_vowels(string),expected_result)

		string = "A nice day to code!"
		expected_result = 8
		self.assertEqual(count_vowels(string),expected_result)

	def test_if_returns_the_count_of_all_consonants_in_the_string(self):
		string = "Python"
		expected_result = 4
		self.assertEqual(count_consonants(string),expected_result)

		string = "Theistareykjarbunga"
		expected_result = 11
		self.assertEqual(count_consonants(string),expected_result)

		string = "grrrrgh!"
		expected_result = 7
		self.assertEqual(count_consonants(string),expected_result)

		string = "Github is the second best thing that happend to programmers, after the keyboard!"
		expected_result = 44
		self.assertEqual(count_consonants(string),expected_result)

		string = "A nice day to code!"
		expected_result = 6
		self.assertEqual(count_consonants(string),expected_result)


	def test_if_returns_a_dictionary_from_string(self):
		string = "Python!"
		expected_result = {'h': 1, 'n': 1, 'o': 1, 't': 1, 'y': 1, 'P': 1, '!': 1}
		self.assertEqual(char_histogram(string),expected_result)

	def test_if_returns_the_sum_of_all_numbers_in_the_matrix(self):
		m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
		expected_result = 45
		self.assertEqual(sum_matrix(m),expected_result)

		m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
		expected_result = 0
		self.assertEqual(sum_matrix(m),expected_result)

		m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
		expected_result = 55
		self.assertEqual(sum_matrix(m),expected_result)

	def test_if_returns_the_expansion_of_NaN_n_times(self):
		n = 0
		expected_result = ""
		self.assertEqual(nan_expand(n),expected_result)

		n = 1
		expected_result = "Not a NaN"
		self.assertEqual(nan_expand(n),expected_result)

		n = 2
		expected_result = "Not a Not a NaN"
		self.assertEqual(nan_expand(n),expected_result)

		n = 3
		expected_result = "Not a Not a Not a NaN"
		self.assertEqual(nan_expand(n),expected_result)

	def test_when_takes_an_integer_and_returns_a_list_of_tuples_that_is_the_result_of_the_factorization(self):
		n = 10
		expected_result = "[(2, 1), (5, 1)]"
		self.assertEqual(prime_factorization(n),expected_result)

		n = 14
		expected_result = "[(2, 1), (7, 1)]"
		self.assertEqual(prime_factorization(n),expected_result)

		n = 356
		expected_result = "[(2, 2), (89, 1)]"
		self.assertEqual(prime_factorization(n),expected_result)

		n = 89
		expected_result = "[(89, 1)]"
		self.assertEqual(prime_factorization(n),expected_result)

		n = 1000
		expected_result = "[(2, 3), (5, 3)]"
		self.assertEqual(prime_factorization(n),expected_result)


	def test_when_takes_a_list_of_things_and_returns_a_list_of_group_where_each_group_is_formed_by_all_equal_consecutive_elements_in_the_list(self):
		n = [1, 1, 1, 2, 3, 1, 1]
		expected_result = [[1, 1, 1], [2], [3], [1, 1]]
		self.assertEqual(group(n),expected_result)

		n = [1, 2, 1, 2, 3, 3]
		expected_result = [[1], [2], [1], [2], [3, 3]]
		self.assertEqual(group(n),expected_result)

	def test_when_which_takes_a_list_of_things_and_returns_an_integer_the_count_of_elements_in_the_longest_subsequence_of_equal_consecutive_elements(self):
		n = [1, 2, 3, 3, 3, 3, 4, 3, 3]
		expected_result = 4
		self.assertEqual(max_consecutive(n),expected_result)


		n = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]
		expected_result = 3
		self.assertEqual(max_consecutive(n),expected_result)

	def test_if_returns_True_when_word_is_substring_of_another_word_or_False_when_it_is_not(self):
		substring = "aba"
		string = "bababa"
		expected_result = True
		self.assertEqual(substr(substring, string),expected_result)

		substring = "aba"
		string = "vaaav vavav "
		expected_result = False
		self.assertEqual(substr(substring, string),expected_result)

	def test_when_returns_reversed_word(self):
		word = "baba"
		expected_result = "abab"
		self.assertEqual(reverse_word(word),expected_result)

	def test_when_returns_count_of_a_word_in_horizontal_rows_in_matrix_left_to_right_and_right_to_left(self):
		word = "ivan"
		matrix = ["ivan","navi","inav","mvvn","qrit"]
		expected_result = 2
		self.assertEqual(horizontal(word, 5, 4, matrix),expected_result)

	def test_when_returns_count_of_a_word_in_vertical_cols_in_matrix_left_to_right_and_right_to_left(self):
		word = "ivan"
		matrix = ["ivan","vava","anav","nvvi","qrit"]
		expected_result = 2
		self.assertEqual(vertical(word, 5, 4, matrix),expected_result)


	def test_when_returns_transposed_matrix(self):
		word = "ivan"
		matrix = ["ivan","vava","anav","nvvi","qrit"]
		expected_result = [['i', 'v', 'a', 'n', 'q'], ['v', 'a', 'n', 'v', 'r'], ['a', 'v', 'a', 'v', 'i'], ['n', 'a', 'v', 'i', 't']]
		self.assertEqual(transpose(matrix),expected_result)

	def test_when_returns_square_matrix_from_matrix_n_x_m(self):
		matrix = ["ivan","vava","anav","nvvi","qrit"]
		expected_result = [['i', 'v', 'a', 'n', ''], ['v', 'a', 'v', 'a', ''], ['a', 'n', 'a', 'v', ''], ['n', 'v', 'v', 'i', ''], ['q', 'r', 'i', 't', '']]
		self.assertEqual(to_square(5, 4, matrix),expected_result)


	def test_when_returns_count_of_a_word_in_diagonals_in_matrix_left_to_right_and_right_to_left(self):
		word = "ivan"
		matrix = ["iaai","avva","aaaa","naan","nban"]
		expected_result = 2
		self.assertEqual(diagonals(word, 5, 4, matrix),expected_result)


	def test_when_which_takes_a_matrix_with_symbols_and_word_and_returns_count_of_the_word(self):
		word = "ivan"
		matrix = ["ivan","evnh","inav","mvvn", "qrit"]
		expected_result = 3
		self.assertEqual(word_counter(word, 5, 4, matrix),expected_result)




	
if __name__ == '__main__':
	unittest.main()
