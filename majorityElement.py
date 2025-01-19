def majorityElement(nums):
    li = {}
    for i in range(0,len(nums)):
        if nums[i] not in li:
            li[nums[i]] = 1
        else:
            li[nums[i]] = li.get(nums[i]) + 1

    for key in li:
        if li[key] > len(nums) / 2 :
            return key

nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))