def canPlaceFlowers(flowerbed, n):
    counter = 0
    length = len(flowerbed)

    for i in range(length):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == length - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            counter += 1

        if counter >= n:
            return True

    return counter >= n



flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed,n))
