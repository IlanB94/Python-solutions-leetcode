class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(head):
        li = []
        while head:
            li.append(head.val)
            head = head.next
        li.sort()
        current = ListNode(0)
        res = current
        while li:
            val = li[0]
            li.remove(li[0])
            current.next = ListNode(val)
            current = current.next
        return res.next

    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)

    n1.next = n2
    n2.next = n3

    print(sortList(n1))