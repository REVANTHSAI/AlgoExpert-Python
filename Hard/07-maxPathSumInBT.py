''''
Write a fucntion that takes in a Binary Tree and returns its maxPathSum. A path
is a collection of connected nodes where no node is connected to more than two
other nodes

Time - O(N)
Space - O(Log N)
''''
def maxPathSum(tree):
	_, maxSum = findMaxSum(tree)
	return maxSum

def findMaxSum(tree):
	if tree == None:
		return (0,0)

	leftMax_sum_asBranch,left_max_path_sum = findMaxSum(tree.left)
	rightMax_sum_asBranch,right_max_path_sum = findMaxSum(tree.right)
	max_child_sum_asBranch = max(leftMax_sum_asBranch,rightMax_sum_asBranch)

	value = tree.value
	max_sum_as_branch = max(max_child_sum_asBranch+value,value)
	max_sum_as_sub_tree = max(max_sum_as_branch,leftMax_sum_asBranch+value+rightMax_sum_asBranch)
	running_max_path_sum = max(left_max_path_sum,right_max_path_sum,max_sum_as_sub_tree)

	return (max_sum_as_branch, running_max_path_sum)
