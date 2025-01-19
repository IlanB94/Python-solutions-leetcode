class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1,l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry

        carry = total // 10
        current.next = ListNode(total % 10)
        current  = current.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next


    return dummy.next



l11 = ListNode(2)
l12 = ListNode(4)
l13 = ListNode(3)

l21 = ListNode(5)
l22 = ListNode(6)
l23 = ListNode(4)

l11.next = l12
l12.next = l13

l21.next = l22
l22.next = l23

addTwoNumbers(l11,l21)

addTwoNumbers(l11,l21)