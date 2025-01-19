class Solution(object):
    def reverse(x):

        isNegative = x < 0

        if isNegative:
            x = x * -1

        temp = 0
        while x > 0:
            temp = temp * 10 + x % 10
            x //= 10

        if temp < -2**31:
            return 0

        if temp > 2**31-1:
            return 0

        if isNegative:
            return temp * -1
        else:
            return temp



    print(reverse(1534236469))