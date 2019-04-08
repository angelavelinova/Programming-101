import sys
import random
def chain(iterable_one, iterable_two):
	iter1 = iter(iterable_one)
	iter2 = iter(iterable_two)
	it1=next(iter1)
	it2=next(iter2)
	return it1, it2
	print(next(iter1),next(iter2))
	#iter1 = next(iter1)
	#iter2 = next(iter2)


def chain(iterable_one, iterable_two):
	n1 = iter(iterable_one)
	n2 = iter(iterable_two)
	while True:
		yield n1,n2
		n1 = next(n1)
		n2 = next(n2)
    
mu = list(chain(range(0,4),range(4,8)))
print(mu)
print(list(chain(range(0,4),range(4,8))))

def chain(iterable1, iterable2):
	for elem in iterable1:
			yield elem
	for elem in iterable2:
			yield elem


#for l in chain(range(0,4), range(4,8)):
#	print(l)
print(list(chain(range(0,4), range(4,8))))


def compress(iterable, mask):
	sety = set()
	for i in range(0,len(mask)):
		if mask[i] == True:
			yield iterable[i]


print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
	
def cycle(iterable):
	while True:
		for elem in iterable:
				yield elem
#endless = cycle(range(0,10))
#for item in endless:
#	print(item)


def chapter_generator(files):
	word = sys.stdin.readline()
	i = 0
	while i < len(files):
		f = open(files[i],'r')
		i = 0
		array = f.readlines()			
		length = len(array)
		while i < length-1:
			if array[i][1]!='c' and array[i][2]!='h':

				print(array[i])
			i+=1
		print(array[i])
		f.close()
		print('\n')

		if(word=="	"):
			yield files[i]
			i += 1

print(list(chapter_generator(["001.txt", "002.txt", "003.txt"])))

def book_generator(count, words):#random-word library

		f = open("book.txt",'a+')
		i = 0
		while i < count:
			f.write("Now the file has more content!")
			i += 1		
		yield f
