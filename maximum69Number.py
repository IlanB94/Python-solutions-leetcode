class Solution(object):
    def maximum69Number (num):
        num_str = str(num)
        mul = len(num_str) - 1
        for i in range(0,len(num_str)):
            if num_str[i] == '9':
                mul -= 1
            else:
                break

        if mul >= 1:
            return num + ((10 ** mul) * 3)
        elif mul == 0:
            return num + 3
        elif mul == -1:
            return num

    print(maximum69Number(66))