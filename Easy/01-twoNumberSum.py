#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

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
