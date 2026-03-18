from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# # naive approach would be to build a joint list and sort it and create a new linked-list:
# def mergeTwoLists(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
#     arr = []

#     while head1 is not None:
#         arr.append(head1.val)
#         head1 = head1.next
    
#     while head2 is not None:
#         arr.append(head2.val)
#         head2 = head2.next

#     arr.sort()

#     dummy = Node(-1)
#     curr = dummy

#     for val in arr:
#         curr.next = Node(val)
#         curr = curr.next
    
#     return dummy.next

# # needed to look for the recursive formulation: O(n+m) time O(n+m) memory
# def mergeTwoLists(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
#     if head1 is None:
#         return head2
#     if head2 is None:
#         return head1
    
#     if head1.val <= head2.val:
#         head1.next = mergeTwoLists(head1.next, head2)
#         return head1
#     else:
#         head2.next = mergeTwoLists(head2.next, head1)
#         return head2
    
# iterative merging O(n+m) time, O(1) memory
def mergeTwoLists(head1: Optional[Node], head2: Optional[Node]) -> Optional[Node]:
    dummy = Node(-1)
    curr = dummy

    while head1 is not None and head2 is not None:
        # add the smaller node to the merged list
        if head1.val <= head2.val:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next

    if head1 is not None:
        curr.next = head1
    else:
        curr.next = head2

    return dummy.next
        


list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)

def printList(node):
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next

printList(mergeTwoLists(list1, list2))
