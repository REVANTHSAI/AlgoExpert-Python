''''
Write a function that takes an array as input and returns max sum and the subSequence
that returns the max sum

A subSequence is defined as a set of numbers that are not necessarily adjacent
but are in the same order as they appear in the input.
Sample Input -
[10,70,20,30,50,11,30]
Sample Output - [110,[10,20,30,50]]
Time - O(N^2)
Space - O(N)
''''

def maxSumIncreasingSubsequence(array):
	sums =[num for num in array]
	subSeqStartIdx = [None for _ in range(len(array))]
	maxSumIndex = 0
	for i in range(len(array)):
		current_num = array[i]
		for j in range(i):
			if array[j] < current_num and sums[j]+current_num >= sums[i]:
				sums[i] = sums[j]+current_num
				subSeqStartIdx[i] = j
		if sums[i] > sums[maxSumIndex]:
			maxSumIndex = i
	maxSubSequenceSum = sums[maxSumIndex]
	maxSubSequence = buildSubSequence(array,subSeqStartIdx,maxSumIndex)
	return [maxSubSequenceSum,maxSubSequence]

def buildSubSequence(array,subSeqStartIdx,currentSumIndex):
	subSequence = []
	while currentSumIndex != None:
		subSequence.append(array[currentSumIndex])
		currentSumIndex = subSeqStartIdx[currentSumIndex]
	return list(reversed(subSequence))
