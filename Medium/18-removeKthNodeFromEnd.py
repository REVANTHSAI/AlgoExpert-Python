# Time complexity O(N)
# Space complexity O(1)
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
	f_pointer = head
	kth_pointer = head
	count = 1
    # Move the kth_pointer k nodes away from the head
    # In list 1->2->3->4 if k=2 , kth_pointer will point to 3
	while count <= k:
		kth_pointer = kth_pointer.next
		count += 1
    #Check the corener case where kth_pointer is already None. In that case delete head node
	if kth_pointer == None:
		head.value = head.next.value
		head.next = head.next.next
		return
    # Once Kth pointer is at k nodes from the head, Move both f_pointer and K_pointer untill kth_pointer.next == None
	while kth_pointer.next != None:
		f_pointer = f_pointer.next
		kth_pointer = kth_pointer.next
	f_pointer.next = f_pointer.next.next
