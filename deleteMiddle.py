# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def deleteMiddle(head):
    pointer = head
    count_number_of_nodes = 0
    while pointer:
        count_number_of_nodes += 1
        pointer = pointer.next
    if count_number_of_nodes <= 1:
        return []
    count_number_of_nodes //= 2

    temp = head
    current = temp
    prev = current
    while count_number_of_nodes > 0:
        count_number_of_nodes -= 1
        prev = current
        current = current.next

    prev.next = current.next

    return temp



n1 = ListNode(1)
n2 = ListNode(3)
n3 = ListNode(4)
n4 = ListNode(7)
n5 = ListNode(1)
n6 = ListNode(2)
n7 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

print(deleteMiddle(n1))
