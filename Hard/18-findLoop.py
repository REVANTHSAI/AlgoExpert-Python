''''
Find is a loop exists in a linked list and return the point of origin of
the loop.

Time - O(N)
Space - O(1)
''''
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    fast_ptr, slow_ptr = head, head
    while fast_ptr.next != None:
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if fast_ptr == slow_ptr:
            break
    if fast_ptr.next != None:
        fast_ptr = head
        while fast_ptr != slow_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        return fast_ptr
    else:
        return None
