''''
Write a function that takes in an array of integers and returns an array of
lengeth 2 representing the largest range of numbers contained in the array.
The furst number in the output array should be the first number in the range
while the second number should be the last number in the range.

Sample Input - [1,11,3,0,15,5,2,4,10,7,12,6]
Output - [0,7]
''''
# Space O(N) | Time O(N)
def largestRange(array):
	bestRange = []
	longestLength = 0
	numbers = {}
    for num in array:
		numbers[num] = True

	for num in array:
		if numbers[num] == False:
			continue
		numbers[num] = False
		current_len = 1
		prev_num = num-1
		next_num = num+1
		while prev_num in numbers:
			numbers[prev_num] = False
			prev_num = prev_num - 1
			current_len += 1
		while next_num in numbers:
			numbers[next_num] = False
			next_num = next_num + 1
			current_len += 1
		if current_len > longestLength:
			longestLength = current_len
			bestRange = [prev_num+1,next_num-1]
	return bestRange
