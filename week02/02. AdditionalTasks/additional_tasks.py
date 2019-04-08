import sys
def anagrams():
	word = sys.stdin.readline()
	word1=""
	word2=""
	i = 0
	while word[i] != " " and i < len(word):
		i += 1
		
	j = -1

	while j < len(word)-1:
		j += 1
		if(word[j]!=" "):
			if(j < i):
				word1+=word[j]
			elif j > i:
				word2+=word[j]
	
	word2=word2[0:len(word2)-1]
	if sorted(word1) == sorted(word2):
		return "ANAGRAMS"
	else:
		return "NOT ANAGRAMS"

def anagrams(word1, word2):
	if sorted(word1) == sorted(word2):
		return "ANAGRAMS"
	else:
		return "NOT ANAGRAMS"
#print(anagrams())

#10.Credit card validation
def sum_digits(number):
	sum_digits = 0
	while number > 0:
		sum_digits += number % 10
		number //= 10
	return sum_digits

def is_credit_card_valid(number):
	number = str(number)
	new_number = ""
	i = len(number)-1
	while i >= 0:
		if i % 2 == 0:
			new_number += number[i]
			i -= 1
		else:
			new_number += str(int(number[i])*2)
			i -= 1
	if(sum_digits(int(new_number)))%10 == 0:
		return True
	return False

#11.Goldbach Conjecture
def is_prime(n):
	if n==1:
		return False
	if n == 2:
		return True
	for i in range(2,n):
		if n % i == 0:
			return False
	return True 

def exist_in(element,array):
	i = 0
	while i < len(array):
		if element == array[i]:
			return True
		i += 1
	return False

def goldbach(n):
	already_printed = []
	result = []
	if n == 1 or n == 2:
		print("Number must be greater than 2 !")
	else:
		i = 2
		while i < n:
			if is_prime(i) and is_prime(n-i) and not(exist_in(i,already_printed)) and not(exist_in(n-i,already_printed)):
				result.append((i, n-i))
				already_printed.append(i)
				already_printed.append(n-i)
			i += 1
	return result
