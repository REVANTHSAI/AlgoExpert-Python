# Time - O(N) Space - O(1)
def reverseLinkedList(head):
	p1,p2 = None,head
	while p2 != None:
		p3 = p2.next
		p2.next = p1
		p1 = p2
		p2 = p3
	head = p1
	return head
