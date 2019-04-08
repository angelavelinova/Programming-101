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

def delete_new_line(string):
	string=string[0:len(string)-1]
	return string

def filter(filename, **kwargs):
	f = open(filename,'r')
	array = f.readlines()
	a = array[0].split(',')
	a.append("order_by")
	i = 1
	result = []
	a[len(a)-2] = delete_new_line(a[len(a)-2])
	sort = False
	while i < len(array):
		len_kwargs = 0
		j = 0
		while j < len(a):
			if substr(a[j], str(kwargs)) and a[j]=="order_by":
				sort = True
				len_kwargs += 1

			elif substr(a[j], str(kwargs)) and not substr(a[j]+"__startswith", str(kwargs)) and not substr(a[j]+"__contains", str(kwargs)) and not substr(a[j]+"__gt", str(kwargs)) and not substr(a[j]+"__lt", str(kwargs)):
				if substr(kwargs[a[j]],array[i]):
					len_kwargs += 1
			elif substr(a[j]+"__startswith", str(kwargs)) and not substr(a[j]+"__contains", str(kwargs)) and not substr(a[j]+"__gt", str(kwargs)) and not substr(a[j]+"__lt", str(kwargs)):
				if a[j]=="full_name":
					if substr(kwargs[a[j]+"__startswith"]+" ",array[i]):
						len_kwargs += 1
				if a[j]=="favourite_color":
					if substr(kwargs[a[j]+"__startswith"]+"",array[i]):
						len_kwargs += 1
			elif substr(a[j]+"__contains", str(kwargs)) and not substr(a[j]+"__gt", str(kwargs)) and not substr(a[j]+"__lt", str(kwargs)):
				if substr(""+kwargs[a[j]+"__contains"]+"",array[i]):
					len_kwargs += 1

			elif substr(a[j]+"__gt", str(kwargs)) or substr(a[j]+"__lt", str(kwargs)):
				a_split=array[i].split(',')
				salary= delete_new_line(a_split[len(a_split)-1])
				if substr(a[j]+"__gt", str(kwargs)):
					if kwargs[a[j]+"__gt"]<int(salary):
						len_kwargs += 1
				if substr(a[j]+"__lt", str(kwargs)):
					if kwargs[a[j]+"__lt"]>int(salary):
						len_kwargs += 1

			j += 1

		if len_kwargs == len(kwargs):
			result.append(array[i])
		i += 1
	f.close()
	if sort == True:
		#print("SORT")
		len_result=len(result)
		new_res=[]
		for l in range(0,len_result):
			current = result[l].split(',')
			if len(current) > 6:
				new_current=[]
				m = 0
				while m < len(current):
					if m <= 2 or m >= len(current)-3:
						new_current.append(current[m])
						m += 1
					else:
						new_current[2]+=current[m]
						m += 1
				current = new_current
			new_res.append(current)
		if kwargs['order_by'] == "salary":
			indy = len(new_res[0])-1
		if kwargs['order_by'] == "phone_number":
			indy = len(new_res[0])-2
		if kwargs['order_by'] == "email":
			indy = len(new_res[0])-3
		if kwargs['order_by'] == "company_name":
			indy = 2
		if kwargs['order_by'] == "favourite_color":
			indy = 1
		if kwargs['order_by'] == "full_name":
			indy = 0

		result = sorted(new_res,key=lambda x:x[indy])
	return result

def count(filename,**kwargs):
	return len(filter(filename,**kwargs))

def first(filename,**kwargs):
	result = filter(filename,**kwargs)
	return result[0]

def last(filename,**kwargs):
	result = filter(filename,**kwargs)
	return result[len(result)-1]
