# monotonically decreasing(increasing) stack

# putting index into the stack
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result


# putting index into the stack
def next_smaller_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result


print(next_greater_element([1, 2, 3, 4, 5]))

print(next_smaller_element([1, 2, 3, 4, 5]))
print(next_smaller_element([3, 2, 1]))
