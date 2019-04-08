import sys
#1.Sum of all digits of a number
def sum_of_digits(n):
	n = abs(n)
	summy = 0
	while n != 0:
		summy += n % 10
		n = n // 10
	return summy

#2.1 Turn a number into list of digits
def len_digits(n):
	length = 0
	while n > 0:
		n = n//10
		length = length + 1
	return length

def to_digits(number):
	lst = []
	str_number=str(number)
	lenny = len(str_number)
	i = 0
	while i < lenny:
		lst.append(int(str_number[i]))
		i += 1

	return lst

#2.2 Turn a list of digits into a number
def to_number(digits):
	number = 0
	length = len(digits)
	i = 0
	while i < length:
		if(digits[i] == 0): 
			number = number * 10
			i = i + 1
		else:
			number_of_digits = len_digits(digits[i])
			number = number * (10 ** number_of_digits) + digits[i]
			i = i + 1
	return number

#3.Factorial Digits
def fact(n):
	if(n==0 or n==1):
		return 1
	else:
		return n*fact(n-1)

def fact_digits(n):
	n = abs(n)
	summy = 0
	while n != 0:
		last = n % 10
		summy += fact(last)
		n = n // 10
	return summy

#4.Palindrome
def palindrome(n):
	n=str(n)
	copy_n = n
	len_n = len(n)
	i = 0
	is_palindrome = True
	middle = len_n//2
	while i < middle:
		if(n[i]!=n[len_n-i-1]):
			is_palindrome=False
		i = i+1
	return is_palindrome

#5.Vowels in a string
def count_vowels(str):
	len_str=len(str)
	i = 0
	vowels_counter = 0
	str=str.lower()
	while i < len_str:
		if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='y'):
			vowels_counter += 1
		i += 1
	return vowels_counter

#6.Consonants in a string
def count_consonants(str):
	len_str=len(str)
	i = 0
	vowels_counter = 0
	str=str.lower()
	while i < len_str:
		if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u' or str[i]=='y' or ord(str[i]) < 97 or ord(str[i]) > 122):
			i+=1
		else:
			vowels_counter += 1
			i += 1
	return vowels_counter

#7.Char Histogram
def char_histogram(string):
	result = {  'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,
				'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0, 'w': 0,'x': 0,'y': 0,'z': 0,'d': 0,
				'A': 0,'B': 0,'C': 0,'D': 0,'E': 0,'F': 0,'G': 0,'H': 0,'I': 0,'J': 0,'K': 0,
				'L': 0,'M': 0,'N': 0,'O': 0,'P': 0,'Q': 0,'R': 0,'S': 0,'T': 0,'U': 0,'V': 0, 'W': 0,'X': 0,'Y': 0,'Z': 0,
				'.': 0,'!': 0,'?': 0,',': 0,':': 0,';': 0,
	}
	len_str=len(string)
	i=0
	while i < len_str:
		result[string[i]] +=1
		i += 1
	for k in list(result):
		if(result[k]==0):
			del result[k]
	return result

#8.Sum Numbers in Matrix
def sum_matrix(m):
	N=len(m)
	M=len(m[0])
	sum_mat = 0
	i = 0
	j = 0
	for i in range(0,N):
		for j in range(0,M):
			sum_mat += m[i][j]
	return sum_mat

#9.NaN Expand
def nan_expand(times):
	result=""
	while(times > 0):
		if (times==1):
			result = result + "Not a NaN"
		else:
			result += "Not a "
		times -= 1
	return result

#10.Integer prime factorization
def is_prime(n):
	flag=True
	if(n==1):
		flag = False
	else:
		i = 2
		while (i < n and flag==True):
			if(n % i == 0):
				flag = False
				break
			else:
				i += 1
	return flag

def prime_factorization(n):
	result = "["
	i = 1
	if(is_prime(n)):
		result += "(" + str(n) + ", " + str(1) + ")]"
	else:
		copy_n=n
		while i < copy_n :
			count = 0
			while n % i == 0 and is_prime(i):
				count += 1
				n //= i
			if(count>0):
				result += "(" + str(i) + ", " + str(count) + ")"
				if(n > 1):
					result += ", "
			i += 1
		result += "]"
	return result

#11.The group function
def group(items):
	result = []
	current_group = [items[0]]
	for i in range(1,len(items)):
		if current_group[-1] == items[i]:
			current_group.append(items[i])
		else:
			result.append(current_group)
			current_group = [items[i]]
	result.append(current_group)
	return result

#12.Longest subsequence of equal consecutive elements
def max_consecutive(items):
	pass
	i = 1
	max_count = 1
	current_count = 1
	current_item = items[0]
	while i < len(items):
		if items[i] == current_item:
			current_count += 1
			i += 1
			if current_count > max_count:
				max_count = current_count
		else:
			current_count=1
			current_item = items[i]
			i += 1
	return max_count

#13.Word counter
def substr(substring, string):
	i = 0
	j = 0
	flag = False
	while j < len(string) and i < len(substring):
		if substring[i]!=string[j]:
			i = 0
			j += 1
		else:
			i += 1
			j += 1
		if i == len(substring):
			flag = True
	
	return flag

def reverse_word(word):
	rev = ""
	i = len(word)-1
	while i >= 0:
		rev += word[i]
		i -= 1
	return rev

def horizontal(word, rows, cols, matrix):
	count = 0
	word_ind = 0
	i = 0
	while i < rows:
		if(substr(word, matrix[i])):
			count += 1
		if(substr(reverse_word(word), matrix[i])):
			count += 1
		i += 1
	j = 0;
	return count

def transpose(matrix):
	rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
	return rez

def to_square(rows, cols, matrix):
	maxi = max(rows,cols)
	new_matrix = [["" for i in range(maxi)] for j in range(maxi)]
	for i in range(rows):
		for j in range(cols):
			new_matrix[i][j] = matrix[i][j]
	return new_matrix 

def vertical(word, rows, cols, matrix):
	transposed_matrix = transpose(to_square(rows,cols,matrix))
	count = 0
	word_ind = 0
	i = 0
	while i < max(rows,cols):
		if(substr(word, transposed_matrix[i])):
			count += 1
		if(substr(reverse_word(word), transposed_matrix[i])):
			count += 1
		i += 1
	return count
 
def diagonals(word, rows, cols, matrix):
	count = 0
	current_diag = ""
	square_matrix=to_square(rows,cols,matrix)
	#left - > right
	n = max(rows,cols)
	for k in range(0,n):
		i = k
		while i >= 0:
			current_diag += square_matrix[i][k-i]
			i -= 1
		if substr(word,current_diag):
			count += 1

		if substr(word,reverse_word(current_diag)):
			count += 1
		current_diag = "" 

	n = min(rows,cols)
	for k in range(n,2*n):
		i = n
		while i >= k - n + 1:
			current_diag += square_matrix[i][k-i]
			i -= 1
		if substr(word,current_diag):
			count += 1
		if substr(word,reverse_word(current_diag)):
			count += 1
		current_diag = ""

	#right - > left
	n = max(rows,cols)
	k = n - 1
	while k >= 0:
		for i in range(k,n):
			current_diag += square_matrix[i][i-k]

		if substr(word,current_diag):
			count += 1
		if substr(word,reverse_word(current_diag)):
			count += 1
		current_diag = ""
		k -= 1  

	n = min(rows,cols)
	k = -1
	while k >= 1-n:
		for i in range(0,n+k):
			current_diag += square_matrix[i][i-k]

		if substr(word,current_diag):
			count += 1
		if substr(word,reverse_word(current_diag)):
			count += 1
		current_diag = ""
		k -= 1
	return count

def word_counter(word, rows, cols, matrix):
	if len(word)>rows or len(word)>cols:
		print("Invalid number of rows or columns!")
	else:
		counter = 0
		counter += horizontal(word, rows, cols, matrix) + vertical(word, rows, cols, matrix) + diagonals(word, rows, cols, matrix)
		return counter
