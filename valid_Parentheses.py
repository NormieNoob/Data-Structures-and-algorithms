def valid_parentheses(s: str) -> bool:
    #Creating an empty stack
    stack = []

    #if the length of the string is not even, return false
    if not len(s) % 2 == 0:
        return False

    #storing the closing brackets as the key & opening brack as the value
    sMap = {")": "(", "]": "[", "}": "{"}

    for i in s:
        #pushing all the opening bracket directly into the stack
        if i not in sMap:
            stack.append(i)
        else:
            '''
            if it's a closing bracket & if the stack is not empty 
            & if the top element of the stack is respective opeing bracket
            then will pop the last element of the stack
            '''
            if stack and stack[-1] == sMap[i]:
                stack.pop()
            else:
                return False

    #return true if stack is empty
    return True if not stack else False

