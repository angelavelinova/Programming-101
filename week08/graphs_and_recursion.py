from collections.abc import Iterable

#1.1.
def dfs_rec_deep_find(data,key):
	for edge in data:
		if type(edge) == str and edge == key:
			return data[key]

		if type(data[edge]) == dict:
			if dfs_rec_deep_find(data[edge],key) != None:
				return dfs_rec_deep_find(data[edge],key)

		if type(data[edge]) == list or type(data[edge]) == set:
			for i in range(len(data[edge])):
				for k in data[edge][i]:
					res = dfs_rec_deep_find(data[edge][i],key)
					if res != None:
						return res

		if type(data[edge]) == tuple:
			for i in range(1):
				res = dfs_rec_deep_find(data[edge][0],key)
				if res != None:
					return res
          
#1.2.
def bfs_rec_deep_find(data, key):
	data_list = []
	for edge in data:
		if edge == key:
			return data[edge]
		elif isinstance(data[edge],dict):
			data_list.append(data[edge])
		elif isinstance(data[edge], Iterable):
			data_list.append(data[edge])
		
	while True:
		for element in data_list:
			if isinstance(element,dict):
				for k in element:
					if k == key:
						return element[k]
					elif isinstance(element[k],dict):
						data_list.append(element[k])
					elif isinstance(element[k], Iterable):
						for e in element[k]:
							if isinstance(e,dict):
								data_list.append(e)
								
			elif isinstance(element, Iterable):
				for e in element:
					if isinstance(e,dict):
						 data_list.append(e)
					elif isinstance(e,Iterable):
						for el in e:
							if isinstance(el,dict):
								data_list.append(el)

def clean(array):
	result = []
	string = str(array)
	current = ""
	i = 0
	while i  < len(string):
		if string[i] == "'":
			i += 1
			while string[i] != "'":
				current += string[i]
				i += 1
			if current not in result:
				result.append(current)
			current = ""
		i += 1

	return result

#2.1.
def dfs_rec_deep_find_all(data,key):
	result = []
	for edge in data:
		if isinstance(edge,str) and edge == key:
			result.append(data[key])

		elif isinstance(data[edge],dict):
			if dfs_rec_deep_find_all(data[edge],key) != None:
				result.append(dfs_rec_deep_find_all(data[edge],key))

		elif isinstance(data[edge],list) or isinstance(data[edge],set):
			for i in range(len(data[edge])):
				for k in data[edge][i]:
					res = dfs_rec_deep_find_all(data[edge][i],key)
					if res != None:
						result.append(res)
						
		elif isinstance(data[edge],tuple):
			res = dfs_rec_deep_find_all(data[edge][0],key)
			if res != None:
				result.append(res)
			res = dfs_rec_deep_find_all(data[edge][1],key)
			if res != None:
				result.append(res)

	result = clean(result)
	return result

#2.2.
def bfs_rec_deep_find_all(data, key):
	result = []
	data_list = []
	for edge in data:
		if edge == key:
			return data[edge]
		elif isinstance(data[edge],dict):
			data_list.append(data[edge])
		elif isinstance(data[edge], Iterable):
			data_list.append(data[edge])
		
		for element in data_list:
			if isinstance(element,dict):
				for k in element:
					if k == key:
						result.append(element[k])
						#print(result)
					elif isinstance(element[k],dict):
						data_list.append(element[k])
					elif isinstance(element[k], Iterable):
						for e in element[k]:
							if isinstance(e,dict):
								data_list.append(e)
								
			elif isinstance(element, Iterable):
				for e in element:
					if isinstance(e,dict):
						 data_list.append(e)
					elif isinstance(e,Iterable):
						for el in e:
							if isinstance(el,dict):
								data_list.append(el)

	return result

#3.
def deep_update(data, key, val):
	data_list = []
	for edge in data:
		if edge == key:
			data[edge] = val
		elif isinstance(data[edge],dict):
			data_list.append(data[edge])
		elif isinstance(data[edge], Iterable):
			data_list.append(data[edge])
		
		for element in data_list:
			if isinstance(element,dict):
				for k in element:
					if k == key:
						element[k] = val
						#print(result)
					elif isinstance(element[k],dict):
						data_list.append(element[k])
					elif isinstance(element[k], Iterable):
						for e in element[k]:
							if isinstance(e,dict):
								data_list.append(e)
								
			elif isinstance(element, Iterable):
				for e in element:
					if isinstance(e,dict):
						 data_list.append(e)
					elif isinstance(e,Iterable):
						for el in e:
							if isinstance(el,dict):
								data_list.append(el)

	return data

#4.
def deep_apply(func, data):
	new = {}
	data_list = []
	for edge in data:
		new_data = {func(edge): data[edge]}
		new.update(new_data)
		if isinstance(data[edge],dict):
			data_list.append(data[edge])
		elif isinstance(data[edge], Iterable):
			data_list.append(data[edge])
		
		for element in data_list:
			if isinstance(element,dict):
				for k in element:
					new_data = {func(k): element[k]}
					new.update(new_data)
					if isinstance(element[k],dict):
						data_list.append(element[k])
					if isinstance(element[k], Iterable):
						for e in element[k]:
							if isinstance(e,dict):
								data_list.append(e)
								
			elif isinstance(element, Iterable):
				for e in element:
					if isinstance(e,dict):
						 data_list.append(e)
					elif isinstance(e,Iterable):
						for el in e:
							if isinstance(el,dict):
								data_list.append(el)
	data = new
	return data

def func(a):
	return str(a)+'!!!'

#5.
def deep_compare(obj1, obj2):
	data_list1 = []
	data_list2 = []
	for edge1 in obj1:
		if isinstance(obj1[edge1],dict):
			data_list1.append(obj1[edge1])
		elif isinstance(obj1[edge1], Iterable):
			data_list1.append(obj1[edge1])
			
	for edge2 in obj2:
		if isinstance(obj2[edge2],dict):
			data_list2.append(obj2[edge2])
		elif isinstance(obj2[edge2], Iterable):
			data_list2.append(obj2[edge2])
		
		for element in data_list1:
			if isinstance(element,dict):
				for k in element:
					if isinstance(element[k],dict):
						data_list1.append(element[k])
					elif isinstance(element[k], Iterable):
						for e in element[k]:
							if isinstance(e,dict):
								data_list1.append(e)
								
			elif isinstance(element, Iterable):
				for e in element:
					if isinstance(e,dict):
						 data_list1.append(e)
					elif isinstance(e,Iterable):
						for el in e:
							if isinstance(el,dict):
								data_list1.append(el)

		for element in data_list2:
			if isinstance(element,dict):
				for k in element:
					if isinstance(element[k],dict):
						data_list1.append(element[k])
					elif isinstance(element[k], Iterable):
						for e in element[k]:
							if isinstance(e,dict):
								data_list2.append(e)
								
			elif isinstance(element, Iterable):
				for e in element:
					if isinstance(e,dict):
						 data_list2.append(e)
					elif isinstance(e,Iterable):
						for el in e:
							if isinstance(el,dict):
								data_list2.append(el)

	return data_list1 == data_list2

#6.
def read_keys_from_list(listy):
	result = []
	for l in listy:
		if isinstance(l, str):
			result.append(l)
		elif isinstance(l, list):
			result.append(read_keys_from_list(l))
	return clean(result)

def read_keys_from_dictionary(dicty):
	result = []
	for d in dicty:
		if isinstance(d, str) and isinstance(dicty[d], str):
			result.append(d)
		if not isinstance(dicty[d], str):
			result.append(d)
			result.append(read_keys_from_dictionary(dicty[d]))
	return clean(result)

def schema_validator(schema: list, data: dict):
	if not (isinstance(schema, list) or (data, dict)):
		raise TypeError
	return read_keys_from_list(schema) == read_keys_from_dictionary(data)
