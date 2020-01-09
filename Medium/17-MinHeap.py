"""
Min-Heap
1. A min-heap is a binary tree such that the data contained in each node is less
than(or equal to) the data in that node’s children.
2. the binary tree is complete
3. Root node is the min element in the tree

Max-Heap
1. A max-heap is a binary tree such that the data contained in each node
is greater than (or equal to) the data in that node’s children.
2. the binary tree is complete
3. Root node is the max element in the tree

Heap can be represented as an array -


Note -
- A full binary tree (sometimes proper binary tree or 2-tree) is a tree in which
  every node other than the leaves has two children.
- A complete binary tree is a binary tree in which every level, except possibly
  the last, is completely filled, and all nodes are as far left as possible.
"""

# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
		first_parent_index = (len(array)-2) // 2
		for current_index in reversed(range(first_parent_index+1)):
			self.siftDown(current_index,len(array)-1,array)
        return array

    def siftDown(self,current_index,end_index,heap):
		child_one_index = 2 * current_index + 1
		while child_one_index <= end_index:
			child_two_index = 2 * current_index + 2 if 2 * current_index + 2 <= end_index else -1
			if child_two_index != -1 and heap[child_one_index] > heap[child_two_index]:
				index_to_swap = child_two_index
			else:
				index_to_swap = child_one_index
            if heap[current_index] > heap[index_to_swap]:
                self.swap(current_index,index_to_swap,heap)
                current_index = index_to_swap
                child_one_index = 2 * current_index + 1
            else:
                return

    def siftUp(self,current_index,heap):
		parent_index = (current_index - 1) // 2
		while parent_index >= 0 and heap[parent_index] > heap[current_index]:
			self.swap(parent_index,current_index,heap)
			current_index = parent_index
			parent_index = (current_index-1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
		last_index = len(self.heap)-1
		self.swap(0,last_index,self.heap)
		value_to_remove = self.heap.pop(last_index)
		self.siftDown(0,len(self.heap)-1,self.heap)
		return value_to_remove

    def insert(self, value):
		self.heap.append(value)
		self.siftUp(len(self.heap)-1,self.heap)

	def swap(self,i,j,heap):
		if i != j:
			heap[i],heap[j] = heap[j],heap[i]
