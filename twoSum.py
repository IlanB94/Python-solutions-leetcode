def twoSum(nums, target):
    li = []
    for i in range(0, len(nums)):
        result = target-nums[i]
        if result in nums and i != nums.index(result):
            li = [0] * 2
            li[0] = i
            li[1] = nums.index(result)
            return li
    return li



nums = [3,2,4]
target = 6
print(twoSum(nums, target))
