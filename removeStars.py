def removeStars(s):
    stack = []
    i = 0
    for char in s:
        if char == '*':
            stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)




s = "erase*****"
print(removeStars(s))