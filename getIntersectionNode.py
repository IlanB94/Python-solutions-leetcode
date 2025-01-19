class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        pointer1 = headA
        pointer2 = headB

        while pointer1 != pointer2:
            if pointer1:
                pointer1 = pointer1.next
            else:
                pointer1 = headB
            if pointer2:
                pointer2 = pointer2.next
            else:
                pointer2 = headA
        return pointer1


