def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    return haystack.index(needle)

haystack = "leetcode"
needle = "leeto"
print(strStr(haystack,needle))

