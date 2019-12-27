# Write a function that takes a Binary Tree and return a list of its branch sums
# Time Complexity - O(N) The code has to reverse through all the nodes to calculate the branch sum
# Space Complexity - Space for reccursive call in the stack space + Space for saving sum in List = O(Log N) + O(N/2) = O(N)

# For Reccursive function call stack - O(Log N)
# For saving the sums in the list the size of the array should be equal to the number of leaf nodes
# On average the number of leaf nodes in a Binary tree = N/2. So, Space complexity is - O(N/2)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
	sum_list = []
    return branchSums_reccursive_helper(root,sum_list,current_sum = 0)

# In reccusrive call we need to pass the current_ sum and the sum_list down the tree.
def branchSums_reccursive_helper(current_node,sum_list,current_sum):

    # If node is null return.(To handle cases where left or right nodes are null)
	if current_node == None:
		return

	current_sum += current_node.value

    # On reaching a leaf node. Append the sum to the sum list
	if current_node.left == None and current_node.right== None:
		sum_list.append(current_sum)

	branchSums_reccursive_helper(current_node.left,sum_list,current_sum)
	branchSums_reccursive_helper(current_node.right,sum_list,current_sum)
	return sum_list
