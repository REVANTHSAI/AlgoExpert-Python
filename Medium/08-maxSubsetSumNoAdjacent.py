# Dynamic Programming
# Time O(N) Space - O(N)
# This narrows down to MAXSUM[i] = MAX(MAXSUM[i-1],MAXSUM[i-2]+ARR[i])
def maxSubsetSumNoAdjacent(array):
	if not array:
		return 0
	elif len(array) == 1:
		return array[0]
	sum_array = array[:]
	sum_array[0] = array[0]
	sum_array[1] = max(array[0],array[1])
	for i in range(2,len(array)):
		sum_array[i] = max(sum_array[i-1],sum_array[i-2]+array[i])
	return sum_array[-1]
# No need to save the max sum at every position. Instead jus save MAXSUM[i-1],MAXSUM[i-2] in two temporary variables.
# Time - O(N) Space - O(1)
def maxSubsetSumNoAdjacent(array):
	if not array:
		return 0
	elif len(array) == 1:
		return array[0]
	first = array[0]
	second = max(array[0],array[1])
	current = 0
	for i in range(2,len(array)):
		current = max(second,first+array[i])
		first = second
		second = current
	return second
