# Worst Case Complexity - Space - O(N^2) | Time - O(N^3) (When Hash table has N pairs mapped to a single sum value)
# Average Case Complexity - Space - O(N^2) | Time O(N^3) 
def fourNumberSum(array, targetSum):
	result = []
    sum_map = {}
	for i in range(1,len(array)-1):
		for j in range(i+1,len(array)):
			current_sum = array[i]+array[j]
			diff = targetSum-current_sum
			if diff in sum_map:
				for pair in sum_map[diff]:
					result.append(pair+[array[i],array[j]])
		for k in range(i):
			two_num_sum = array[k]+array[i]
			if two_num_sum in sum_map:
				sum_map[two_num_sum].append([array[i],array[k]])
			else:
				sum_map[two_num_sum] = [[array[i],array[k]]]
	return result
