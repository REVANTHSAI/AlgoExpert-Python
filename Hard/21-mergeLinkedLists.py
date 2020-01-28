''''
Time - O(N+M), Space - O(1)
''''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
	l1_prev, l1_current = None, headOne
	l2_current= headTwo
	while l2_current != None and l1_current != None:
		if l2_current.value <= l1_current.value:
			if l1_prev != None:
				l1_prev.next = l2_current
			l1_prev = l2_current
			l2_current = l2_current.next
			l1_prev.next = l1_current
		else:
			l1_prev = l1_current
			l1_current = l1_current.next
	if l1_current == None:
		l1_prev.next = l2_current
	return headOne if headOne.value < headTwo.value else headTwo
