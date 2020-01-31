
# Reccursive Solution
# Time - O(Log N) | Space - O(Log N)

def shiftedBinarySearch(array, target):
    return shiftedBinarySearch_helper(array,target,0,len(array)-1)

def shiftedBinarySearch_helper(array,target,first_index,last_index):
    if first_index > last_index:
        return -1
    middle_index = (first_index + last_index) // 2
    if array[middle_index] == target:
        return middle_index
    elif array[first_index] <= array[middle_index]:
        if target < array[middle_index] and target >= array[first_index]:
            return shiftedBinarySearch_helper(array,target,first_index,middle_index-1)
        else:
            return shiftedBinarySearch_helper(array,target,middle_index+1,last_index)
    else:
        if target > array[middle_index] and target <= array[last_index]:
            return shiftedBinarySearch_helper(array,target,middle_index+1,last_index)
        else:
            return shiftedBinarySearch_helper(array,target,first_index,middle_index-1)

# Iterative Solution
# Time - O(Log N) | Space - O(1)

def shiftedBinarySearch(array, target):
    first_index = 0
    last_index = len(array)-1
    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if array[middle_index] == target:
            return middle_index
        elif array[first_index] <= array[middle_index]:
            if target < array[middle_index] and target >= array[first_index]:
                last_index = middle_index-1
            else:
                first_index = middle_index+1
        else:
            if target > array[middle_index] and target <= array[last_index]:
                first_index = middle_index+1
            else:
                last_index = middle_index-1
    return -1
