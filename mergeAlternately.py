def mergeAlternately(word1, word2):
    lenA = len(word1)
    lenB = len(word2)
    newStr = ""
    if lenA > lenB:
        maximumLength = lenA
    else:
        maximumLength = lenB
    maxLength = maximumLength * 2
    flag = 0
    for i in range(0,maxLength):
        if flag == 0 and len(word1) != 0:
            newStr += word1[0]
            word1 = word1[1::]
            flag = 1
        elif flag == 1 and len(word2) != 0:
            newStr += word2[0]
            word2 = word2[1::]
            flag = 0
        else:
            if len(word1) == 0:
                newStr += word2
                break
            if len(word2) == 0:
                newStr += word1
                break
    return newStr


word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1,word2))

