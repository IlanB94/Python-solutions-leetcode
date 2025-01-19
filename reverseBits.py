class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(n):
        bin_rep = bin(n)[2:].zfill(32)
        reversed_bin = bin_rep[::-1]

        return int(reversed_bin,2)






    n = 10
    print(reverseBits(n))
