''''
Write a function that takes in an array of integers of lengeth at least 2.
The function should return an array of starting and ending incides of the
smallest subarray in the input array that needs to be sorted in place in order
for the entire input array to be sorted. If the input array is already sorted
function should return [-1,-1]

Solution -
O(1) - Space | O(N) - Time
1. Calculate the minOutOfOrder and maxOutOfOrder number in the array
2. Calculate the index of the minOutOfOrder and maxOutOfOrder in the input array
3. These indexes are the starting and ending of the subarray that needs to be sorted
   for the entire array to be sorted.
''''
def subarraySort(array):
    minOutOfOrder = float('inf')
	maxOutOfOrder = float('-inf')
	for i in range(len(array)):
		if isNumOutOfOrder(i,array):
			if array[i] < minOutOfOrder:
				minOutOfOrder = array[i]
			if array[i] > maxOutOfOrder:
				maxOutOfOrder = array[i]
	if minOutOfOrder == float('inf'):
		return [-1,-1]

	subArrayLeftIndex = 0
	while minOutOfOrder >= array[subArrayLeftIndex]:
		subArrayLeftIndex += 1

	subArrayRightIndex = len(array)-1
	while maxOutOfOrder <= array[subArrayRightIndex]:
		subArrayRightIndex -= 1

	return [subArrayLeftIndex,subArrayRightIndex]

def isNumOutOfOrder(index,array):
	num = array[index]
	if index == len(array)-1:
		return num < array[index-1]
	elif index == 0:
		return num > array[index+1]
	else:
		return (num < array[index-1] or num > array[index+1])
