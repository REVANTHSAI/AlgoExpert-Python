# Binary Search Tree Construction (Insert, Delete and Contains operations)
# Iterative Solution -

# Time Complexity -
# Insertion - Worst Case - O(N), Average  - O(Log N)
# Remove - Worst Case - O(N), Average  - O(Log N)
# Contains - Worst Case - O(N), Average  - O(Log N)
# Space Complexity - O(1) (For reccursive soltution it will be O(Log N))

# Steps to solve this - (Removing a node from BST)
# 1. Traverse the BST and find the node to be removed in the BST
# 2. If current_node to be removed contains a left child and a right child then -
#       * Update the value of the current_node to the leaset value(left most node) in the right sub tree
#       * Delete the left most node in the right subtree
# 3. If current_node to be removed is a root node and doesn't satisfy the above condition then -
#      If current_node.left != None:
#        current_node.value = current_node.left.value
#        current_node.right = current_node.left.right
#        current_node.left =  current_node.left.left
#      Simularly for when current_node.right ! = Non
# 4. If the node to be removed has only one or no child node
#     parent_node.left = current_node.left if current_node.left != None else current_node.right
#     parent_node.right = current_node.left if current_node.left != None else current_node.right

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
		current_node = self
		while current_node != None:
			parent_node = current_node
			if value >= current_node.value:
				current_node = current_node.right
			else:
				current_node = current_node.left
		if value >= parent_node.value:
			parent_node.right = BST(value)
		else:
			parent_node.left = BST(value)
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def contains(self, value):
		current_node = self
		while current_node != None:
			if value > current_node.value:
				current_node = current_node.right
			elif value < current_node.value:
				current_node = current_node.left
			else:
				return True
		return False

    def remove(self, value):
		parent_node = None
		current_node = self
		while current_node != None:
			if value > current_node.value:
				parent_node = current_node
				current_node = current_node.right
			elif value < current_node.value:
				parent_node = current_node
				current_node = current_node.left
			else:
				# If the node two be removed has two child nodes
				if current_node.left != None and current_node.right != None:
					current_node.value = current_node.right.getMinValue()
					current_node.right.remove(current_node.value)

                # If the node to be removed is a root node and doesn't satisfy above condition
				elif parent_node == None:
					if current_node.left != None:
						current_node.value = current_node.left.value
						current_node.right = current_node.left.right
						current_node.left =  current_node.left.left
					elif current_node.right != None:
						current_node.value = current_node.right.value
						current_node.left = current_node.right.left
						current_node.right = current_node.right.right
					else:
						current_node.value = None

                # If the node to be removed has only one or no child node
				elif parent_node.left == current_node:
					parent_node.left = current_node.left if current_node.left != None else current_node.right

				elif parent_node.right == current_node:
					parent_node.right = current_node.left if current_node.left != None else current_node.right
			    break
        return self

	def getMinValue(self):
		node = self
		while node.left != None:
			node = node.left
		return node.value
