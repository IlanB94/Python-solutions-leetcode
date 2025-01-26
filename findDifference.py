
# def findDifference(nums1, nums2):
#     final_li = []
#     li1 = []
#     li2 = []
#     for num in nums1:
#         if num not in nums2 and num not in li1:
#             li1.append(num)
#     for num in nums2:
#         if num not in nums1 and num not in li2:
#             li2.append(num)
#     final_li.append(li1)
#     final_li.append(li2)
#     return final_li

#Another solution:
def findDifferenceV2(nums1,nums2):
    li1 = list(set(nums1) - set(nums2))
    li2 = list(set(nums2) - set(nums1))
    return [li1,li2]


nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifferenceV2(nums1,nums2))