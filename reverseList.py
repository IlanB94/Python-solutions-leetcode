# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Correct print function
    def print_nodes(self):
        current = self  # Start from the current node
        while current:
            print(current.val, end=" -> " if current.next else "\n")
            current = current.next  # Move to the next node

def reverseList(head):
    prev = None  # This will become the new head
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
result = reverseList(n1)
