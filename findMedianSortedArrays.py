class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMedianSortedArrays(self,nums1,nums2):
    joined_list = nums1 + nums2
    joined_list.sort()
    if len(joined_list) % 2 == 0:
        exp1 = joined_list[((len(joined_list)) // 2 - 1)]
        exp2 = joined_list[((len(joined_list) // 2))]
        result = (exp1 + exp2) / 2.0
        return result
    return joined_list[((len(joined_list))//2)]





num1 = [1,2]
num2 = [3,4]
print(findMedianSortedArrays(1,num1,num2))