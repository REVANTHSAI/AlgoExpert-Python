# Sample Input - [12,3,1,2,-6,5,-8,6],0
# Sample Output - [[-8,2,6],[-8,3,5],[-6,1,5]]
# Time - O(N^2)
# Space - O(N)
def threeNumberSum(array, targetSum):
	array.sort()
    p1 = 0
	output = []
	while p1 < len(array)-2:
		p2 = p1+1
		p3 = len(array)-1
		while p2 < p3:
			current_sum = array[p1]+array[p2]+array[p3]
			if current_sum == targetSum:
				output.append([array[p1],array[p2],array[p3]])
				p2 += 1
				p3 -= 1
			elif current_sum > targetSum:
				p3 -= 1
			elif current_sum < targetSum:
				p2 += 1
		p1 += 1
	return output
