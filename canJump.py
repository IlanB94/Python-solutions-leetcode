def canJump(nums):
    target_number_index = len(nums) - 1
    for i in range(len(nums) - 2, -1,-1):
        if target_number_index <= i + nums[i]:
            target_number_index = i
    return target_number_index == 0






nums = [2,3,1,1,4]
print(canJump(nums))