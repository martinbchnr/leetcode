from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
    carry = 0

    dummy = Node(-1)
    curr = dummy

    while l1 is not None and l2 is not None:
        val = l1.val + l2.val + carry
        print(f"  {val}")
        if val >= 10:
            carry = 1
            val = val - 10
        curr.next = Node(val)
        curr = curr.next
        l1 = l1.next
        l2 = l2.next

    printList(dummy)
    print(carry)
    print("\n")
    
    if l1 is not None:
        while l1 is not None:
            val = l1.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            curr.next = Node(val)
            l1 = l1.next
            curr = curr.next

    if l2 is not None:
        while l2 is not None:
            val = l2.val + carry
            if val >= 10:
                carry = 1
                val = val - 10
            curr.next = Node(val)
            l2 = l2.next
            curr = curr.next
    
    print("done with both l1 and l2")
    
    if carry > 0:
        curr.next = Node(carry)

    return dummy.next



list1 = Node(9)
list1.next = Node(9)
list1.next.next = Node(9)
list1.next.next.next = Node(9)

list2 = Node(9)
list2.next = Node(9)
list2.next.next = Node(9)
list2.next.next.next = Node(9)
list2.next.next.next.next = Node(9)
list2.next.next.next.next.next = Node(9)
list2.next.next.next.next.next.next = Node(9)

def printList(node):
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next

printList(addTwoNumbers(list1, list2))
        