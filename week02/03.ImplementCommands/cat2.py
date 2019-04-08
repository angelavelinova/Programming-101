import sys
from cat import *


def cat2(arguments):
	for i in range(1,len(arguments)- 1):
		cat(arguments[i])
		print("\n")
	i += 1
	cat(arguments[i])

def main():
	arguments = sys.argv
	cat2(arguments)

if __name__ == '__main__':
	main()
