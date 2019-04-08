import math
def delete_two_positions(array, position):
	result = []
	i = 0
	while i < len(array):
		if i != position and i != position - 1:
			result.append(array[i])
		i += 1
	return result

def delete_element(array, position):
	result = []
	i = 0
	while i < len(array):
		if i != position:
			result.append(array[i])
		i += 1
	return result

def rpn_calculate(expr):
	split_expr = expr.split(' ')
	i = 0
	while 1 < len(split_expr):
		if split_expr[i] == '+':
			split_expr[i-2] = str(float(split_expr[i-2]) + float(split_expr[i-1]))
			split_expr=delete_two_positions(split_expr, i)
			i = 0

		elif split_expr[i] == '-':
			split_expr[i-2] = str(float(split_expr[i-2]) - float(split_expr[i-1]))
			split_expr=delete_two_positions(split_expr, i)
			i = 0

		elif split_expr[i] == '/':
			split_expr[i-2] = str(float(split_expr[i-2]) / float(split_expr[i-1]))
			split_expr=delete_two_positions(split_expr, i)
			i = 0

		elif split_expr[i] == '*':
			split_expr[i-2] = str(float(split_expr[i-2]) * float(split_expr[i-1]))
			split_expr=delete_two_positions(split_expr, i)
			i = 0
		elif split_expr[i] == '^':
			split_expr[i-2] = str(float(split_expr[i-2]) ** float(split_expr[i-1]))
			split_expr=delete_two_positions(split_expr, i)
			i = 0

		elif split_expr[i] == 'sqrt':
			split_expr[i-1] = str(math.sqrt(float(split_expr[i-1])))
			split_expr=delete_element(split_expr, i)
			i = 0

		elif split_expr[i] == 'max':
			j = i - 1
			array = []
			while split_expr[j].isdigit():
				array.append(split_expr[j])
				j -= 1
			j += 1
			m = max(array)
			split_expr[j] = str(m)
			while i > j:
				split_expr=delete_element(split_expr, i)
				i -= 1
			i = 0

		elif split_expr[i] == 'min':
			j = i - 1
			array = []
			while split_expr[j].isdigit():
				array.append(split_expr[j])
				j -= 1
			j += 1
			m = min(array)
			split_expr[j] = str(m)
			while i > j:
				split_expr=delete_element(split_expr, i)
				i -= 1
			i = 0
		i += 1


	return str(float(split_expr[0]))
