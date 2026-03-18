from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    if head is None:
        return False

    slow_iter = head
    fast_iter = head.next.next

    while slow_iter != fast_iter:
        if slow_iter is None or fast_iter is None:
            return False
        slow_iter = slow_iter.next
        fast_iter = fast_iter.next.next

    return True

# Create the linked list nodes
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = head

print(hasCycle(head))