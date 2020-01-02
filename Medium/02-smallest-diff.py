#Write a function that take two non-empty array of integers and find the pair of numbers
#whose absolute difference is close to zero
# Sample Input - [-1,5,10,20,28,3],[26,134,135,15,17]
# Sample Output - [28,26]
# Time O(NLogN)+O(MLogM)+O(N+M) = O(NLogN)+O(MLogN)
# Space O(1)
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	p1,p2 = 0,0
	smallest = []
	smallest_diff = float('inf')
	current_diff = float('inf')
	while p1 < len(arrayOne) and p2 < len(arrayTwo):
		first_num = arrayOne[p1]
		second_num = arrayTwo[p2]
		current_diff = abs(arrayOne[p1]-arrayTwo[p2])
		if arrayOne[p1] > arrayTwo[p2]:
			p2 += 1
		elif arrayOne[p1] < arrayTwo[p2]:
			p1 += 1
		else:
			return [first_num,second_num]
		if smallest_diff > current_diff:
			smallest_diff = current_diff
			smallest = [first_num,second_num]
	return smallest
