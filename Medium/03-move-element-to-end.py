# You are given an array if integers. Write function to move all instances of that integer in the array to the end of the array.
# Sample Input - [2,1,2,2,2,3,4,2]
# Out Put - [1,3,4,2,2,2,2,2]
# Time Complexity - O(N)
# Space Complexity - O(1)

def moveElementToEnd(array, toMove):
	if len(array) == 0:
		return array

	left_ptr = 0
	right_ptr = len(array)-1

	while left_ptr < right_ptr:
        # Move right pointer to an element that is != toMove
		while array[right_ptr] == toMove and left_ptr < right_ptr:
				right_ptr -= 1
        # Move left pointer to an element = toMove.
        # Swap the left pointer and right pointer elements
		if array[left_ptr] == toMove:
			array[left_ptr],array[right_ptr] = array[right_ptr],array[left_ptr]
		left_ptr += 1
	return array
