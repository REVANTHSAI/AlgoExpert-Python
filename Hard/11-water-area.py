# Question - https://leetcode.com/problems/container-with-most-water/
# Time Complexity - O(N)
# Space Complexity - O(1)
def waterArea(heights):
	left_ptr = 0
	right_ptr = len(heights)-1
	left_max = 0
	right_max = 0
	total = 0
	while left_ptr < right_ptr:
		if heights[left_ptr] < heights[right_ptr]:
			if heights[left_ptr] > left_max:
				left_max = heights[left_ptr]
			else:
				total = total + left_max - heights[left_ptr]
			left_ptr += 1
		else:
			if heights[right_ptr] > right_max:
				right_max = heights[right_ptr]
			else:
				total = total + right_max - heights[right_ptr]
			right_ptr -= 1
	return total
