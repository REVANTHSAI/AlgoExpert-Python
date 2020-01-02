# Given a binary tree, validate that it is a binary search tree.
# This is an input class. Do not edit.
#Time - O(N)
#Space - O(H)
#H - Height of the BST
# Note- Based on the property of a BST, We can say that every node has a min and max possible value.
# If the node value doesn't agree to the above condition we can say that the given binary tree is a BST.

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	return validateBst_helper(tree,float('-inf'),float('inf'))

def validateBst_helper(tree,min_value,max_value):
	if tree == None:
		return True
	if tree.value < min_value or tree.value >= max_value:
		return False
	left_is_valid = validateBst_helper(tree.left,min_value,tree.value)
	right_is_valid = validateBst_helper(tree.right,tree.value,max_value)
	return left_is_valid and right_is_valid
