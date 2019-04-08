import sys
from random import randint


def generate_numbers(filename, numbers):
	f = open(filename,'w')
	i = 0
	while i < int(numbers):
		f.write(str(randint(1, 1000)))
		f.write('\t')
		i+=1
	f.close()


def main():
	arguments = sys.argv
	generate_numbers(arguments[1],arguments[2])
	

if __name__ == '__main__':
	main()
