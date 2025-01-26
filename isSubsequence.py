def isSubsequence(s, t):
    if len(s) == 0:
        return True
    index = 0
    for i in range(len(t)):
        if s[index] == t[i]:
            index += 1
            if index == len(s):
                return True
    return False


s = "axc"
t = "ahbgdc"
print(isSubsequence(s,t))