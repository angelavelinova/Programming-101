#1.Implement the cat command - Print file contents
print("1.Implement the cat command - Print file contents")
import sys
def delete_new_line(string):
	string=string[0:len(string)-1]
	return string

def cat(arguments):
	f = open(arguments,'r')
	i = 0
	array = f.readlines()
	length = len(array)
	while i < length-1:
		print(delete_new_line(array[i]))
		i+=1
	print(array[i])
	f.close()

def main():
	arguments = sys.argv[1]
	cat(arguments)

if __name__ == '__main__':
	main()
