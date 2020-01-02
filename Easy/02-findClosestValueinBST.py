#Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
# Iterative Solution
# Average Time Complexity O(Log N)
# Worst Case time Complexity O(N)
# Space Complexity O(1)
def findClosestValueInBst(tree, target):
	closest_value = float('inf')
	current_node = tree
    # Write your code here.
	while current_node != None:
		# Compare closest value to the value of current node
		# If the value of the current node is closer. Update the closer node
    	if abs(target-current_node.value) < abs(target-closest_value):
			closest_value = current_node.value

		if target < current_node.value:
			current_node = current_node.left

		elif target > current_node.value:
			current_node = current_node.right
		# If targer is equal to the current node. Then we can break and return closest Node
		else:
			break
	return closest_value


# Reccursive Solution
def findClosestValueInBst(tree, target):
	return findClosestValueInBst_Helper(tree,target,closest = float('inf'))

def findClosestValueInBst_Helper(tree,target,closest):
	# Write your code here.
	if tree == None:
		return closest
	if abs(target - closest) > abs(target - tree.value):
		closest = tree.value
	if target > tree.value:
		return findClosestValueInBst_Helper(tree.right,target,closest)
	elif target < tree.value:
		return findClosestValueInBst_Helper(tree.left,target,closest)
    else:
		return closest
