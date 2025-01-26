def moveZeroes(nums):
    position = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position] = nums[i]
            position += 1

    for i in range(position,len(nums)):
        nums[i] = 0
    return nums




nums = [1,0,1]


print(moveZeroes(nums))