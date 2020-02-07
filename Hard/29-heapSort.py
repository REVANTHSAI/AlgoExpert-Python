'''
Worst, Average, Best -
Time - O(N Log N) (Time take to sift N node in the heap)
Space - O(1) (Sort Happens inline)
'''
def heapSort(array):
    build_heap(array)
	for end_indx in reversed(range(1,len(array))):
		swap(array,0,end_indx)
		sift_down(array,0,end_indx-1)
	return array

def build_heap(array):
	last_parent_node = len(array)-2//2
	for current_index in reversed(range(last_parent_node+1)):
		sift_down(array,current_index,len(array)-1)

def sift_down(array,current_index,last_index):
	left_child_index = 2*current_index+1
	while left_child_index <= last_index:
		right_child_index = 2*current_index+2 if 2*current_index+2 <= last_index else -1
		if right_child_index != -1 and array[right_child_index] > array[left_child_index]:
			index_to_swap = right_child_index
		else:
			index_to_swap = left_child_index
		if array[current_index] < array[index_to_swap]:
			swap(array,current_index,index_to_swap)
			current_index = index_to_swap
			left_child_index = 2*current_index+1
		else:
			return

def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
