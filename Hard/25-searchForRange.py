#Time - O(Log N) Space - O(Log N)
def searchForRange(array, target):
    search_range = [-1,-1]
    modifiedBinarySearch(array,target,search_range,0,len(array)-1,True)
    modifiedBinarySearch(array,target,search_range,0,len(array)-1,False)
    return search_range

def modifiedBinarySearch(array,target,search_range,left,right,goLeft):
    if left > right:
        return
    mid = (left+right) // 2
    if array[mid] > target:
        modifiedBinarySearch(array,target,search_range,left,mid-1,goLeft)
    elif array[mid] < target:
        modifiedBinarySearch(array,target,search_range,mid+1,right,goLeft)
    else:
        if goLeft:
            if mid == 0 or array[mid-1] != target:
                search_range[0] = mid
            else:
                modifiedBinarySearch(array,target,search_range,left,mid-1,goLeft)
        else:
            if mid == len(array)-1 or array[mid+1] != target:
                search_range[1] = mid
            else:
                modifiedBinarySearch(array,target,search_range,mid+1,right,goLeft)


#Time - O(Log N) Space - O(1)
def searchForRange(array, target):
    search_range = [-1,-1]
    modifiedBinarySearch(array,target,search_range,0,len(array)-1,True)
    modifiedBinarySearch(array,target,search_range,0,len(array)-1,False)
    return search_range

def modifiedBinarySearch(array,target,search_range,left,right,goLeft):
    while right >= left:
        mid = (left+right) // 2
        if array[mid] > target:
            right = mid-1
        elif array[mid] < target:
            left = mid+1
        else:
            if goLeft:
                if mid == 0 or array[mid-1] != target:
                    search_range[0] = mid
					return
                else:
                    right = mid-1
            else:
                if mid == len(array)-1 or array[mid+1] != target:
                    search_range[1] = mid
					return
                else:
                    left = mid+1
