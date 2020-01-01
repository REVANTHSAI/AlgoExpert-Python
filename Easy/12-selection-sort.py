#The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order) from unsorted part and putting it at the beginning.
#The algorithm maintains two subarrays in a given array.
#1) The subarray which is already sorted.
#2) Remaining subarray which is unsorted.

#In every iteration of selection sort, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.
# Best Case - O(N^2) Space - O(1)
# Worst Case - O(N^2) Space - O(1)
# Average Case - O(N^2) Space - O(1)
def selectionSort(array):
    i = 0
	while i < len(array):
		min_element = i
		j = i+1
		while j < len(array):
			if array[min_element] > array[j]:
				min_element = j
			j += 1
		swap(array,i,min_element)
		i += 1
	return array

def swap(array,i,min_element):
	array[i],array[min_element] = array[min_element],array[i]
