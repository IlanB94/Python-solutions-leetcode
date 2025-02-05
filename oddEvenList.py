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

def oddEvenList(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Running the function and printing the result
result = oddEvenList(n1)
result.print_nodes()
