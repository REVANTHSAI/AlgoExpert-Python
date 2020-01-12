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
