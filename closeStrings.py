def closeStrings(word1, word2):
    my_dict1 = {}
    my_dict2 = {}
    for i in word1:
        if i not in my_dict1:
            my_dict1[i] = 1
        else:
            my_dict1[i] += 1
    for i in word2:
        if i not in my_dict2:
            my_dict2[i] = 1
        else:
            my_dict2[i] += 1

    for char in my_dict1:
        my1 = my_dict1[char]
        my2 = my_dict2[char]
        if my_dict1[char] != my_dict2[char]:
            return False

    return True

word1 = "cabbba"
word2 = "abbccc"

print(closeStrings(word1,word2))

