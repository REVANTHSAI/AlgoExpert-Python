# Time - O(N) Space - O(1)
def hasSingleCycle(array):
	num_visited = 0
	FIRST_ELEMENT = 0
	current_index = 0
	while num_visited < len(array):
		if num_visited > 0 and current_index == 0:
			return False
		num_visited += 1
		current_index = getNextIndex(array,current_index)
	return current_index == FIRST_ELEMENT

def getNextIndex(array,current_index):
	jump =  array[current_index]
	next_index = (current_index + jump) % len(array)
	if next_index < 0:
		next_index = next_index + len(array)
	return next_index
