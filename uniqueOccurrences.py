
def uniqueOccurrences(arr):
    my_dict = {}
    for num in arr:
        if num not in my_dict:
            my_dict[num] = 1
        else:
            my_dict[num] += + 1
    occurances = list(my_dict.values())
    return len(occurances) == len(set(arr))


print(uniqueOccurrences(arr = [1,2,2,1,1,3]))
