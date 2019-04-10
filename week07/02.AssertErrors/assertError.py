def my_sum(num1, num2):
  if num1<0 or num2<0:
		raise ValueError('Only positive integers')
	return num1+num2

@contextmanager
def assertRaises(expected_exception_class, msg = None):
	try:
		yield
		raise Exception ("Exception not found")
	except Exception as exc:
		if type(exc) == expected_exception_class:
			if msg is not None and msg == str(exc):
				return True
			else:
				raise Exception("message is wrong")
		raise Exception('Exception found, but is not {exc}'.format(exc = expected_exception_class))

with assertRaises(ValueError, 'Only positive integers'):
	my_sum(-1,2)
  


#with assertRaises(ValueError):
#	my_sum(-1,2)

#with assertRaises(TypeError, "wrong mmsg"):
#	my_sum(-1,2)
