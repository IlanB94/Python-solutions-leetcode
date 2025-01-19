class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(list1, list2):
        if not list1 == 0:
            return list2
        if not list2:
            return list1
        current = ListNode(0)
        head = current
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

            if list1:
                current.next = list1
            elif list2:
                current.next= list2

        return head.next


    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(4)

    n4 = ListNode(1)
    n5 = ListNode(3)
    n6 = ListNode(4)

    n1.next = n2
    n2.next = n3

    n4.next = n5
    n5.next = n6

    mergeTwoLists(n1,n4)