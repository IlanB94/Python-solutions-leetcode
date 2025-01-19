class Solution(object):
    def intersect(nums1, nums2):

        count1 = {}
        for num in nums1:
            count1[num] = count1.get(num, 0) + 1

        intersection = []
        for num in nums2:
            if num in count1 and count1[num] > 0:
                intersection.append(num)
                count1[num] -= 1  # Decrement the count

        return intersection



    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(intersect(nums1,nums2))