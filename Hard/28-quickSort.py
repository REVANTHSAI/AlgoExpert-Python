''''
Average -
Space - O(Log N) - (Since this is a reccursive Solution)
Time - O(N Log N)

Worst -
Space - O(Log N)
Time - O(N^2)
''''

def quickSort(array):
	quickSort_helper(array,0,len(array)-1)
	return array

def quickSort_helper(array,start_index,end_index):
	if start_index >= end_index:
		return array
	left_pointer = start_index+1
	right_pointer = end_index
	piviot_pointer = start_index
	while right_pointer >= left_pointer:
		if array[left_pointer] > array[piviot_pointer] and array[right_pointer] < array[piviot_pointer]:
			swap(array,left_pointer,right_pointer)
			left_pointer += 1
			right_pointer -= 1
		if array[left_pointer] <= array[piviot_pointer]:
			left_pointer += 1
		if array[right_pointer] >= array[piviot_pointer]:
			right_pointer -= 1
	swap(array,piviot_pointer,right_pointer)
	is_left_subarray_smaller = end_index - (right_pointer+1) >  (right_pointer-1) - start_index

# The below condition is to make the smaller subarray tail reccursive
	if is_left_subarray_smaller:
		quickSort_helper(array,right_pointer+1,end_index)
		quickSort_helper(array,start_index,right_pointer-1)
	else:
		quickSort_helper(array,start_index,right_pointer-1)
		quickSort_helper(array,right_pointer+1,end_index)

def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
