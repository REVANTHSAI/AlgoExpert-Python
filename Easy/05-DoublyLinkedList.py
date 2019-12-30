# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # O(1) Time | O(1) Space
    def setHead(self, node):
		if self.head == None:
			self.head = node
			self.tail = node
			return
		self.insertBefore(self.head,node)

    # O(1) Time | O(1) Space
    def setTail(self, node):
		if self.tail == None:
			self.setHead(node)
			return
		self.insertAfter(self.tail,node)

    # O(1) Time | O(1) Space
    def insertBefore(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.next = node
		nodeToInsert.prev = node.prev
		if node.prev == None:
			self.head = nodeToInsert
		else:
			node.prev.next = nodeToInsert
		node.prev = nodeToInsert

    # O(1) Time | O(1) Space
    def insertAfter(self, node, nodeToInsert):
		if nodeToInsert == self.head and nodeToInsert == self.tail:
			return
		self.remove(nodeToInsert)
		nodeToInsert.next = node.next
		nodeToInsert.prev = node
		if node.next == None:
			self.tail = nodeToInsert
		else:
			node.next.prev = nodeToInsert
		node.next = nodeToInsert

    # O(P) Time | O(1) Space
    def insertAtPosition(self, position, nodeToInsert):
		if position == 1:
			self.setHead(nodeToInsert)
			return
		node = self.head
		current_pos = 1
		while node != None and current_pos != position:
			node = node.next
			current_pos += 1
		if node != None:
			self.insertBefore(node, nodeToInsert)
		else:
			self.setTail(nodeToInsert)

    # O(N) Time | O(1) Space
    def removeNodesWithValue(self, value):
		f_pointer = self.head
		while f_pointer != None:
			node_to_remove = f_pointer
			f_pointer = f_pointer.next
			if node_to_remove.value == value:
				self.remove(node_to_remove)

    # O(1) Time | O(1) Space
    def remove(self, node):
		if node == self.head:
			self.head = self.head.next
		if node == self.tail:
			self.tail = self.tail.prev
		self.removeNodeBindings(node)

    # O(N) Time | O(1) Space
    def containsNodeWithValue(self, value):
		node = self.head
		while node != None and node.value != value:
			node = node.next
		return node != None

	def removeNodeBindings(self,node):
		if node.next != None:
			node.next.prev = node.prev
		if node.prev != None:
			node.prev.next = node.next
		node.next = None
		node.prev = None
