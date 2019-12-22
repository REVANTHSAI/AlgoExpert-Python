#Time Complexity - O(N)
#Space Complexity - O(N)
def twoNumberSum(array, targetSum):
    # Write your code here.
    map = {}
    for i in range(len(array)):
        diff = targetSum-array[i]
        if diff in map:
            return [array[i],diff]
        else:
			map[array[i]] = True
    return []


if __name__ == '__main__':
    array =[3,5,-4,8,11,1,-1,6]
    targetSum = 10
    print(twoNumberSum(array,targetSum))
