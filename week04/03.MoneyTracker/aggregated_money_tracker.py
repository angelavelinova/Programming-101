from parse_money_tracker_data import *

class Aggregated_object():
	def __init__(self):
		pass
	def aggregate_object(self):
		array_data = Data("money_tracker.txt")
		array_data = array_data.data()
		keys = []
		values = []
		i = 0
		val = []
		while i < len(array_data):
			if array_data[i][0] == "=":
				keys.append(array_data[i])
				if val!=[]:
					values.append(val)
					val=[]
			else:
				val.append(array_data[i])
			i += 1
		values.append(val)

		dict_data = dict(zip(keys, values))
		return dict_data
'''
aggregated_object = Aggregated_object()
print(aggregated_object.aggregate_object())
'''
