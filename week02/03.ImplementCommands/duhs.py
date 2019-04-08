import sys
import os
def get_size(start_path):
	size = 0
	for dirpath, dirnames, filenames in os.walk(start_path):
		for f in filenames:
			fp = os.path.join(dirpath, f)
			size += os.path.getsize(fp)
	print(size/1073741824, "G")

def main():
	arguments = sys.argv
	get_size(arguments[1])
	

if __name__ == '__main__':
	main()
