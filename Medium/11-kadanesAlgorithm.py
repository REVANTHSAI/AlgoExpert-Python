# Write a function that takes in a non-empty array of intergers and returns the maximum sum
# that can be obtained by summing all the numbers in a non-empty sub array of the input array.
# Subarray can only contain adjacent numbers
# Input = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
# Output = 19,[1,3,-2,3,4,7,2,-9,6,3,1]
# Time Complexity - O(N)
# Space Complexity - O(1)
def kadanesAlgorithm(array):
	current_sum = array[0]
	max_sum = array[0]
	for i in range(1,len(array)):
		if array[i] > current_sum + array[i]:
			current_sum = array[i]
		else:
			current_sum = current_sum + array[i]
		if current_sum > max_sum:
			max_sum = current_sum
	return max_sum
