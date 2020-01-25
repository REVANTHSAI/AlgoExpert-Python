'''
Calculate the mininmum number of jumps
Sample Input - [3,4,2,1,2,3,7,1,1,1,3]
Sample Output - 4(3->4 or 2->2 or 3->7->3)

Solution 1
Time - O(N^2)
Space - O(N)
'''
def minNumberOfJumps(array):
    # Write your code here.
	jumps = [float("inf") for _ in array]
	jumps[0] = 0
	for i in range(1,len(array)):
		for j in range(i):
			if array[j]+j >= i:
				jumps[i] = min(jumps[i],jumps[j]+1)
	return jumps[-1]
''''
Solution 2
Time - O(N)
Space- O(1)
''''
def minNumberOfJumps(array):
	if len(array)== 1:
		return 0
	min_jumps = 0
	steps = array[0]
	max_reach = array[0]
	for i in range(1,len(array)-1):
		steps -= 1
		max_reach = max(max_reach,array[i]+i)
		if steps == 0:
			min_jumps += 1
			steps = max_reach - i
	return min_jumps+1
