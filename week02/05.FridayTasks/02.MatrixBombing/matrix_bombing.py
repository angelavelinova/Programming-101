import math

def bomb_it(matrix,n, i,j):
	if i == 0 and j == 0:#up left
		matrix[1][0]-=matrix[i][j]
		matrix[0][1]-=matrix[i][j]
		matrix[1][1]-=matrix[i][j]
		#TODO dasi opravq indeksiteee kydeto e n-2
	elif i == n - 1 and j == n - 1:#down right
		matrix[i][j-1]-=matrix[i][j]
		matrix[i-1][j]-=matrix[i][j]
		matrix[i-1][j-1]-=matrix[i][j]
	elif i == n - 1 and j == 0:#down left
		matrix[i-1][j]-=matrix[i][j]
		matrix[i][j+1]-=matrix[i][j]
		matrix[i-1][j+1]-=matrix[i][j]
	elif i == 0 and j == n - 1:#up right
		matrix[i][j-1]-=matrix[i][j]
		matrix[i+1][j-1]-=matrix[i][j]
		matrix[i+1][j]-=matrix[i][j]

	elif i == 0:#zero row
		matrix[i][j-1]-=matrix[i][j]
		matrix[i][j+1]-=matrix[i][j]
		matrix[i+1][j-1]-=matrix[i][j]
		matrix[i+1][j]-=matrix[i][j]
		matrix[i+1][j+1]-=matrix[i][j]

	elif i == n - 1:#zero row
		matrix[i][j-1]-=matrix[i][j]
		matrix[i][j+1]-=matrix[i][j]
		matrix[i-1][j-1]-=matrix[i][j]
		matrix[i-1][j]-=matrix[i][j]
		matrix[i-1][j+1]-=matrix[i][j]

	elif j == 0:#zero row
		matrix[i - 1][0]-=matrix[i][j]
		matrix[i - 1][1]-=matrix[i][j]
		matrix[i][1]-=matrix[i][j]
		matrix[i+1][0]-=matrix[i][j]
		matrix[i+1][1]-=matrix[i][j]

	elif j == n-1:#zero column
		matrix[i - 1][j]-=matrix[i][j]
		matrix[i - 1][j-1]-=matrix[i][j]
		matrix[i][j-1]-=matrix[i][j]
		matrix[i+1][j-1]-=matrix[i][j]
		matrix[i+1][j]-=matrix[i][j]

	else:#is central --> 9 cells
		matrix[i - 1][j]-=matrix[i][j]
		matrix[i + 1][j]-=matrix[i][j]
		matrix[i][j-1]-=matrix[i][j]
		matrix[i][j+1]-=matrix[i][j]
		matrix[i-1][j-1]-=matrix[i][j]
		matrix[i - 1][j+1]-=matrix[i][j]
		matrix[i+1][j-1]-=matrix[i][j]
		matrix[i+1][j+1]-=matrix[i][j]
	summy = 0
	for k in range(0,n):
		for l in range(0,n):
			if matrix[k][l] < 0:
				matrix[k][l] = 0
			summy += matrix[k][l]
	#print(matrix)
	return summy
		
def copy_matrix(m,n):
	copy_m = [[0 for col in range(n)] for row in range(n)]
	for i in range(0,n):
		for j in range(0,n):
			copy_m[i][j] = m[i][j]
	return copy_m	


def matrix_bombing_plan(m):
	n = len(m)
	result_dict = {}
	for i in range(0,n):
		for j in range(0,n):
			result_dict[(i,j)] = 0
	for i in range(0,n):
		for j in range(0,n):
			copy_m = copy_matrix(m,n)
			bomb_m = bomb_it(copy_m,n,i,j)
			result_dict[(i,j)] += int(bomb_m)

	return result_dict
