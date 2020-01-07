# Given a 2d array of distict integers where each row is sorted and each column is sorted
# Write function that retuns an array of row and column indices of the target number.
# Sample Input -
# [[1,4,7,12,15,1000],
# [2,5,19,31,32,1001],
# [3,8,24,33,35,1002],
# [40,41,42,44,45,1003]
# [99,100,103,106,128,1004]],44

# Sample Output -[3,3]
# O(m+n) Time | O(1) Space
def searchInSortedMatrix(matrix, target):
	row = 0
	column = len(matrix[0])-1
	while row < len(matrix) and column >= 0:
		if matrix[row][column] > target:
			column -= 1
		elif matrix[row][column] < target:
			row += 1
		else:
			return [row,column]
	return [-1,-1]
