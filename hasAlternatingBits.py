class Solution(object):
    def hasAlternatingBits(n):
        binary_representation = bin(n)[2:]

        for i in range(0,len(binary_representation)-1):
            if binary_representation[i] == binary_representation[i+1]:
                return False
        return True

    print(hasAlternatingBits(5))


