# Invert a Binary Tree
# Reccursive Solution
# Time - O(N)
# Space - O(d)
def invertBinaryTree(tree):
	if tree == None:
		return
	tree.left,tree.right = tree.right,tree.left
	invertBinaryTree(tree.left)
	invertBinaryTree(tree.right)

# Time - O(N)
# Space - O(N)
def invertBinaryTree(tree):
	queue = [tree]
	while len(queue):
		current = queue.pop(0)
		if current == None:
			continue
		current.left,current.right = current.right,current.left
		queue.append(current.left)
		queue.append(current.right)
