import math


def isPowerOfFour(n):
    base = 4
    if n > 0:
        return (math.log(n,base)).is_integer()
    return False


print(isPowerOfFour(16))