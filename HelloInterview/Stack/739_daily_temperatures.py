# similar to next_greater_element
# the only diff here is the find the diff between i and prev_index in the stack
def daily_temperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []
    for i in range(n):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


print(daily_temperatures([5, 4, 3, 2, 1]))

print(daily_temperatures([1, 4, 5]))
