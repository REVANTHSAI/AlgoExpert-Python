# Write a function that takes in "special" array and returns its product sum
# A special array is a non-empty array that contains either integer or other "Special array"
# "Special" arrays must be summed themselves and multiplied by the depth of the tree
# Product Sum of [x,[y,z]] is x+2y+2z

# Time - O(N), Space - O(D)
# N - Total number of elements in the array
# D - Gratest depth of special array in the array
def productSum(array,level=1):
	total = 0
	for element in array:
		if type(element) == list:
			total += level * productSum(element,level+1)
		else:
			total += level * element
	return total
