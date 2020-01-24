Time - O(N^2)
Space - O(N)
def minNumberOfJumps(array):
    # Write your code here.
	jumps = [float("inf") for _ in array]
	jumps[0] = 0
	for i in range(1,len(array)):
		for j in range(i):
			if array[j]+j >= i:
				jumps[i] = min(jumps[i],jumps[j]+1)
	return jumps[-1]
