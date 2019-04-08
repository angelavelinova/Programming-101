import sys
def count_symbol(symbol, string):
	counter = 0
	for i in range(0,len(string)):
		if string[i]==symbol:
			counter += 1
	return counter

def get_wc(arguments):
	print(arguments)
	print(arguments[1])
	f = open(arguments[1],'r')
	i = 0
	array = f.readlines()
	length = len(array)
	#array=str(array)#array e trite izrecheniq.vsqko e otdelen element v masiva
	#print(length)
	#print(array)
	if(arguments[2]=='lines'):
		print(len(array))
	if(arguments[2]=='words'):
		i = 0
		counter = 0
		while i < len(array):
			counter = count_symbol(' ', array[i]) + count_symbol('\n', array[i])
			i += 1
		print(counter)
	if(arguments[2]=='chars'):
		pass
	
	f.close()


def main():
	arguments = sys.argv
	print(arguments)
	print(get_wc(arguments))
	
if __name__ == '__main__':
	main()
