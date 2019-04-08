def reduce_file_path(path):
	i = len(path)-1
	while i > 1:
		if path[i] == '/' and i == len(path)-1:
			path = path[0:i]
		elif path[i] == '.' and path[i-1] == '.' and i == 2:
			path = '/'
		elif path[i] == '.':
			if path[i-1] == '.':
				while path[i]!='/':
					i -= 1
				path = path[0:i]
				i -= 1
				while path[i]!='/':
					i -= 1
				path = path[0:i+1]
				i -= 1
			if i > 0 and path[i-1] == '/':
				path = path[0:i]
		elif i > 0 and path[i] == '/' and path[i-1] == '/':
			path = path[0:i-1] + path[i:len(path)]

		i -= 1
	if len(path) > 1 and path[0] == path[1] and path[0] == '/':
		path = path[1:len(path)]

	return path
