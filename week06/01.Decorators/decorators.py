import datetime
from time import sleep
import time
def accepts(*args):
	def f(func):
		def calc(*f_args):
			for i in range(0, len(args)):
				if args[i] != type(f_args[i]):
					return TypeError("Argument {!r} of {!r} is not {!r}!".format(i, f.__name__, args[i].__name__))
			return func(*f_args)
			
		return calc 

	return f

@accepts(str)
def say_hello(name):
	return "Hello, I am {}".format(name)

@accepts(str, int)
def deposit(name, money):
	print("{} sends {} $!".format(name, money))
	return True

def encrypt(*args):
	def f(func):
		def calc(*f_args):
			string = func()
			result = ""
			for i in range(0,len(string)):
				if string[i]==" ":
					result+=string[i]
				else:
					code = ord(string[i])+args[0]
					if ord(string[i]) >= 65 and ord(string[i]) <= 90:
						if ord(string[i])+args[0] >= 91:
							while code >= 91:
								code -= 26

					if ord(string[i]) >= 97 and ord(string[i]) <= 122:
						if ord(string[i])+args[0] >= 123:
							while code >= 122:
								code -= 26
					result+=chr(code)

			return result

		return calc

	return f

@encrypt(28)
def get_low():
	return "Get get get lowZz"

#print(get_low("mu"))

def log(*args):
	def f(func):
		def get_low(*f_args):
			string = func()

			fd=open(args[0],'a+')#r+ - chetem i pishem
			fd.write(get_low.__name__)
			fd.write(" was called at ")
			fd.write(str(datetime.datetime.now()))
			fd.write('\n')
			fd.close()

			return string

		return get_low

	return f
@log('log.txt')
@encrypt(28)
def get_low1():
	return "Get get get lowZz"

#print(get_low1())
#print(get_low1())
#print(get_low1())


def performance(*args):
	start = time.time()
	def f(func):
		def something_heavy(*f_args):
			string = func()

			fd=open(args[0],'a+')#r+ - chetem i pishem
			fd.write(something_heavy.__name__)
			fd.write(" was called and took  ")
			end = time.time()
			fd.write(str(end-start))
			fd.write('seconds to complete\n')
			fd.close()

			return string

		return something_heavy

	return f

@performance('log.txt')
def something_heavy():
    sleep(10)
    return "I am done!"

#print(something_heavy())
