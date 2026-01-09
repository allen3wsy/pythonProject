
# stack = []
# stack[-1] means the top of the stack

def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            # len(stack) == 0  also works
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return len(stack) == 0


print(is_valid_parentheses("({)}"))
print(is_valid_parentheses("(){({})}"))
