def is_int(v):
	return str(v).isdigit()

#print(is_int(55))
#print(is_int('a'))

def variable_and_power(s):
	array = s.split('^')
	if len(array) == 1:
		return array[0], 1
	elif len(array) == 2:
		return array[0], int(array[1])

#print(variable_and_power("x^5"))
#print(variable_and_power("x"))

def term(s):
	array = s.split('*')

	if len(array) == 1:
		if is_int(array[0]):
			return int(array[0]), None, None
		else:
			return (1, variable_and_power(array[0])[0], variable_and_power(array[0])[1])
	elif len(array) == 2:
		return (int(array[0]), variable_and_power(array[1])[0], variable_and_power(array[1])[1])

#print(term("4*x^5"))
#print(term("x"))


def coefficient(s):
	array = s.split('*')
	if is_int(array[0]):
		return int(array[0])
	else:
		return 1
#print(coefficient("4*x^5"))
#print(coefficient("x^5"))


class Term:
	def __init__(self, coeff, variable, power):
		if power == 0:
			variable = None

		self.coeff = coeff
		self.variable = variable
		self.power = power

	def __add__(self, other):
		return Term(coeff = self.coeff + other.coeff, variable = self.variable, power = self.power)

	def __eq__(self, other):
		return self.coeff == other.coeff and self.variable == other.variable and self.power == other.power and self.constant == other.constant

	def __str__(self):
		if self.is_constant:
			return str(self.coeff)

		if self.coeff > 1:
			coeff_part = str(self.coeff) + '*'
		else: 
			coeff_part = ''

		if self.power > 1:
			power_part = '^' + str(self.power)
		else:
			power_part = ''
		return str(coeff_part + self.variable + power_part)

	def __repr__(self):
		return str(self)

	def parse_from_string(self, s):
		self.coeff, self.variable, self.power = term(s)

		if self.power is None:
			self.power = 0
		#print("MUUUU", (self.coeff = coeff, self.variable = variable, self.power = power))
		return (self.coeff, self.variable, self.power)

	def constant(self, value):
		self.coeff = value
		self.variable = None
		self.power = 0
		return (self.coeff, self.variable, self.power)

	@property
	def is_constant(self):
		return self.variable is None and self.power == 0

	def derivative(self):
		if self.is_constant:
			return Term.constant(0)

		return Term(coeff = self.coeff * self.power, variable = self.variable, power = max(0, self.power - 1))
