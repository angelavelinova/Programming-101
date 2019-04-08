def simplify_fraction(fraction):
	nominator = fraction[0] 
	denominator = fraction[1]
	if nominator > 0 and denominator > 0:
		if nominator == denominator:
			return (1,1)

		elif nominator % denominator == 0:
			return (denominator//nominator,1)

		elif denominator % nominator == 0:
			return (1,denominator // nominator)

		else:
			i = 2
			while i < nominator:
				if nominator % i == 0 and denominator % i == 0:
					nominator = nominator // i
					denominator = denominator // i
					#print(nominator,denominator,i)
				i += 1
	elif denominator == 0:
		nominator = 0
	return(nominator,denominator)

def collect_fractions(fractions):#fractions is a list of tuples of the form (nominator, denominator).
	i = 0
	result = 0
	pr_den = 1
	while i < len(fractions):
		pr_den *= fractions[i][1]
		i += 1
	nom = 0
	i = 0
	while i < len(fractions):
		nom += fractions[i][0]*(pr_den//fractions[i][1])
		i += 1
	
	return simplify_fraction((nom,pr_den))

def takeFirst(elem):
    return elem[0]
def sort_fractions(fractions):
	i = 0
	result = []
	pr_den = 1
	while i < len(fractions):
		pr_den *= fractions[i][1]
		i += 1
	nom = 0
	i = 0
	while i < len(fractions):
		result.append((fractions[i][0]*(pr_den//fractions[i][1]),pr_den))
		i += 1
	s_result=sorted(result,key=takeFirst)
	i = 0
	ressy=[]
	while i < len(s_result):
		ressy.append(simplify_fraction(s_result[i]))
		i += 1
	return ressy
