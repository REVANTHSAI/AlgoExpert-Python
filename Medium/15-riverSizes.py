# Given a two dimenstional array of unequal height and width containing only 0s and 1s.
# Each 0 represents land and 1 represents part of the river. A river consists of any number of 1s that are wither horizontally
# or vertically adjacent. Write a function that returns an array of size of all rivers represneted in the input matrix.
# Sample Input -
#[[1,0,0,1,0]
#[1,0,1,0,0]
#[0,0,1,0,1]
#[1,0,1,0,1]
#[1,0,1,1,0]]
# Output - [1,2,2,2,5]

# Time - O(W*H) Spcae - O(W*H)
def riverSizes(matrix):
	result = []
	row_len = len(matrix)
	col_len = len(matrix[0])
	visited = [[False for _ in matrix[0]] for _ in matrix]
	for r in range(row_len):
		for c in range(col_len):
			if visited[r][c] == True:
				continue
			traverseNeighbourNodes(matrix,visited,result,r,c)
	return result

# Depth first search to look for 1's in the array.
# All the array indexes which have element 1 and are not visited are added into stack
# Use a Queue instead of a stack for Breadth first search
def traverseNeighbourNodes(matrix,visited,result,r,c):
	river_len = 0
	neighbour_nodes = [[r,c]]
	while neighbour_nodes:
		current_node = neighbour_nodes.pop()
		i = current_node[0]
		j = current_node[1]
		if visited[i][j] == True:
			continue
		visited[i][j] = True
		if matrix[i][j] == 0:
			continue
		river_len += 1
		neighbour = getNeighbourNodes(matrix,visited,i,j)
		neighbour_nodes.extend(neighbour)
	if river_len > 0:
		result.append(river_len)

# Get indexes of all the neighbour nodes.
def getNeighbourNodes(matrix,visited,row,column):
	unvisistedNeighbour = []
	if row > 0 and not visited[row-1][column]:
		unvisistedNeighbour.append([row-1,column])
	if row < len(matrix)-1 and not visited[row+1][column]:
		unvisistedNeighbour.append([row+1,column])
	if column > 0 and not visited[row][column-1]:
		unvisistedNeighbour.append([row,column-1])
	if column < len(matrix[0])-1 and not visited[row][column+1]:
		unvisistedNeighbour.append([row,column+1])
	return unvisistedNeighbour
