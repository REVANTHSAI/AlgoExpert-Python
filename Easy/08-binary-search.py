# Reccursive Solution -
# Time - O(Log N) Space - O(Log N)
def binarySearch(array, target):
	return binarySearch_helper(array,target,0,len(array)-1)

def binarySearch_helper(array,target,left,right):
	if left > right:
		return -1
	mid = left + (right-left)//2
	if target == array[mid]:
		return mid
	elif target < array[mid]:
		return binarySearch_helper(array,target,left,mid-1)
	elif target > array[mid]:
		return binarySearch_helper(array,target,mid+1,right)

# Iterative Solution -
# Time - O(Log N) Space - O(1)
def binarySearch(array, target):
    left = 0
    right = len(array)-1
    while left <= right:
        mid = left + (right-left)//2
        if array[mid] == target:
            return mid
        elif target > array[mid]:
            left = mid+1
        elif target < array[mid]:
            right = mid-1
    return -1
