def longest_valid_parentheses(s):
    max_len = 0
    stack = [-1] # append -1 into stack since in the beginning its valid

    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i) # append i (the starting index where it begins to be valid)
            else:
                max_len = max(max_len, i - stack[-1])

    return max_len

print(longest_valid_parentheses("()"))
print(longest_valid_parentheses("))(())"))