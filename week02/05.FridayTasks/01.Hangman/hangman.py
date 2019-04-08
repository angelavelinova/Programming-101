import sys
def check_and_change(word,current_word,symbol):
	result = ""
	length = len(word)
	for i in range(0,length):
		if symbol != word[i]:
			result+=current_word[i]
		else:
			result+=symbol
	if result==current_word:
		print("Incorrect!")
	return result

def hangman(clue_word):
	counter = 0
	current_word=""
	length = len(clue_word)
	for i in range(0,length):
		#print('_ ', end="", flush=True)
		current_word += "_"
	while current_word != clue_word and counter < 10:
		print(current_word, end="", flush=True)
		print('\n')
		print("Guess a letter:",end="", flush=True)
		symbol = sys.stdin.readline()
		#symbol=symbol[:len(symbol)-1]
		#print("new symbol",ord(symbol))
		#current_word = check_and_change(clue_word,current_word,symbol)
		if current_word == check_and_change(clue_word,current_word, symbol[:len(symbol)-1]):
			counter += 1
		current_word=check_and_change(clue_word,current_word, symbol[:len(symbol)-1])
	if counter >= 10:
		print("You lost!","\n"," _________","\n","|    |    |","\n","|  \ O /  |","\n","|    |    |","\n","|    |    |","\n","|   / \   |")
	else:
		print(current_word)
		print("Congratulations!")
