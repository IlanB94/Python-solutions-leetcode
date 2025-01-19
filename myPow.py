class Solution(object):
    def myPow(x, n):
        if n < -2**31 or n >= 2**31-1:
            return 0
        temp = 1
        if n == 0:
            return 1
        if n > 0:
            while n > 0:
                temp *= x
                n -= 1
            return temp
        else:
            n *= -1
            while n > 0:
                temp *= 1/x
                n -= 1
            return temp
    print(myPow(2,-4))

