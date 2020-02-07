#  Average, Best Case Time - O(N) | Space - O(N)
#  Worst Case - O(N^2) Time | Space - O(N)
#  Reccursive Solution

def quickselect(array, k):
	return quickselect_helper(array,k-1,0,len(array)-1)

def quickselect_helper(array,result_index,start_index,end_index):
	if start_index > end_index:
		raise Exception("Error!")
	piviot_index = start_index
	piviot = array[start_index]
	l_ptr = start_index+1
	r_ptr = end_index
	while l_ptr <= r_ptr:
		if array[l_ptr] >= piviot  and array[r_ptr] < piviot:
			swap(array,l_ptr,r_ptr)
		if array[l_ptr] < piviot:
			l_ptr += 1
		if array[r_ptr] >= piviot:
			r_ptr -= 1
	swap(array,piviot_index,r_ptr)
	if r_ptr == result_index:
		return array[r_ptr]
	if r_ptr <  result_index:
		return quickselect_helper(array,result_index,r_ptr+1,end_index)
	if r_ptr > result_index:
		return quickselect_helper(array,result_index,start_index,r_ptr-1)

def swap(array,one,two):
	array[one],array[two] = array[two],array[one]

# Iterative Solution
#  Average, Best Case Time - O(N) | Space - O(1)
#  Worst Case - O(N^2) Time | Space - O(1)

def quickselect(array, k):
	return quickselect_helper(array,k-1,0,len(array)-1)

def quickselect_helper(array,result_index,start_index,end_index):
	while True:
		if start_index > end_index:
			raise Exception("Error!")
		piviot_index = start_index
		piviot = array[start_index]
		l_ptr = start_index+1
		r_ptr = end_index
		while l_ptr <= r_ptr:
			if array[l_ptr] >= piviot  and array[r_ptr] < piviot:
				swap(array,l_ptr,r_ptr)
			if array[l_ptr] < piviot:
				l_ptr += 1
			if array[r_ptr] >= piviot:
				r_ptr -= 1
		swap(array,piviot_index,r_ptr)
		if r_ptr == result_index:
			return array[r_ptr]
		if r_ptr <  result_index:
			start_index = r_ptr+1
		if r_ptr > result_index:
			end_index = r_ptr-1

def swap(array,one,two):
	array[one],array[two] = array[two],array[one]
