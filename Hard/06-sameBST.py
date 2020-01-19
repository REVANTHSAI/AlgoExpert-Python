''''
Question -
An array of integers is said to represent the BST obtained by inserting each
integer in the array into the BST. Write a functon that takes in two arrays and
return a boolean representing whether or not these arrays represent the same BST.
Sample Input -
[10,15,8,12,94,81,5,2,11] [10,8,5,15,2,12,11,94,81]
Output -
True

Solution 1 -
Time - O(N^2)
Space - O(N^2) + O(D)
- Here O(N^2) for auxilary array space
- O(D) Stack space for reccursive functon call
''''
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
	if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    if arrayOne[0] != arrayTwo[0]:
        return False
    leftOne = getSmaller(arrayOne)
    leftTwo = getSmaller(arrayTwo)
    rightOne = getBiggerEqual(arrayOne)
    rightTwo = getBiggerEqual(arrayTwo)
	return sameBsts(leftOne,leftTwo) and sameBsts(rightOne,rightTwo)

def getSmaller(array):
    smaller = []
    for i in range(1,len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getBiggerEqual(array):
    bigger = []
    for i in range(1,len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger

''''
Solution 2 - (Most Optimal)
Time - O(N^2)
Space - O(D)
- This removes the need for auxilary array space
- O(D) Stack space for reccursive functon call
''''
def sameBsts(arrayOne, arrayTwo):
    return isSameBST(arrayOne,arrayTwo,0,0,float('-inf'),float('inf'))

def isSameBST(arrayOne,arrayTwo,root_index_one,root_index_two,min_val,max_val):
    if root_index_one == -1 or root_index_two == -1:
        return root_index_one == root_index_two
    if arrayOne[root_index_one] != arrayOne[root_index_two]:
        return False

    left_root_arrayOne_index = getIdx_first_smaller(arrayOne,root_index_one,min_val)
    left_root_arrayTwo_index = getIdx_first_smaller(arrayTwo,root_index_one,min_val)
    right_root_arrayOne_index = getIdx_first_LargerEq(arrayOne,root_index_two,max_val)
    right_root_arrayTwo_index = getIdx_first_LargerEq(arrayTwo,root_index_two,max_val)

    current_root = arrayOne[root_index_one]
    left_is_same = isSameBST(arrayOne,arrayTwo, left_root_arrayOne_index, left_root_arrayTwo_index, min_val, current_root)
    right_is_same = isSameBST(arrayOne,arrayTwo, right_root_arrayOne_index, right_root_arrayTwo_index, current_root, max_val)

    return left_is_same and right_is_same

def getIdx_first_smaller(array,start_index,min_val):
    # Find the index of the first smaller value after start_index
    # Make sure the value is greater than or equal to the min_value,
    # Which is the value of previou node in the BST. If it isn't then the
    # value is already located in the left subtree of the previous parent node
    for i in range(start_index+1,len(array)):
        if array[i] < array[start_index] and array[i] >= min_val:
            return i
    return -1


def getIdx_first_LargerEq(array,start_index,max_val):
    # Find the index of the first bigger value after start_index
    # Make sure the value is smaller than the max_val, which is the value of
    # the previous parent node in the BST. If it isn't then the value is
    # located in the right subtree of the previou parent node
    for i in range(start_index+1,len(array)):
        if array[i] >= array[start_index] and array[i] < max_val:
            return i
    return -1
