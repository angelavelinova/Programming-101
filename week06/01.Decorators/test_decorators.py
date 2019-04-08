import unittest
from Decorators import *
class TestDecorators(unittest.TestCase):
	def test_accept_decorator(self):
		self.assertEqual(str(say_hello(4)),str(TypeError("Argument 0 of 'f' is not 'str'!")))
		self.assertEqual(str(say_hello("Hacker")),str("Hello, I am Hacker"))
		self.assertEqual(str(deposit("Roza", 10)),str("True"))

	def test_encrypt_decorator(self):
		self.assertEqual(get_low(),"Igv igv igv nqyBb")

	def test_log_decorator(self):
		pass

	def test_performance_decorator(self):
		pass




	
if __name__ == '__main__':
	unittest.main()
