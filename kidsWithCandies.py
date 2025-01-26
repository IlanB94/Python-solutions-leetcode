def kidsWithCandies(candies, extraCandies):
    li = []
    for i in range(0,len(candies)):
        if candies[i] + extraCandies >= max(candies):
            li.append(True)
        else:
            li.append(False)
    return li



candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies,extraCandies))