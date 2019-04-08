class Data:
	def __init__(self, filename):
		self.file = open(filename)

	def data(self):
		content = self.file.read()
		content = content.split('\n')
		return content

'''
fname = "money_tracker.txt"
rows = Data(fname)
rows = rows.data()
print(rows)
'''
