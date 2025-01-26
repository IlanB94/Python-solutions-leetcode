def maxOperations(nums, k):
    my_dict = {}
    counter = 0
    for num in nums:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] = my_dict.get(num) + 1

    for i in range(0,len(nums)):
        res = k - nums[i]
        if res < 0:
            continue
        if res != k - res:
            if res in my_dict and nums[i] in my_dict:
                if my_dict.get(res) > 0 and my_dict.get(k - res) > 0:
                    if res != k - res:
                        my_dict[res] = my_dict.get(res) - 1
                        my_dict[k - res] = my_dict.get(k - res) - 1
                        counter += 1
                    else:
                        if my_dict.get(res) > 1:
                            my_dict[res] = my_dict.get(res) - 2
                            counter += 1
                if my_dict.get(res) == 0:
                    del my_dict[res]
                if my_dict.get(k - res) == 0:
                    del my_dict[k-res]
        else:
            if my_dict.get(res) > 1:
                my_dict[res] = my_dict.get(res) - 2
                counter += 1

    return counter


nums = [3,1,3,4,3]



k = 6
print(maxOperations(nums,k))