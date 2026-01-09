# Sliding window
# variable-length

def longest_substring_without_repeat(s):
    seen = {}
    max_length = 0
    start = 0

    for end in range(len(s)):
        seen[s[end]] = seen.get(s[end], 0) + 1
        while seen[s[end]] > 1:
            seen[s[start]] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length


print(longest_substring_without_repeat("eghghhgg"))


# using a set is also fine
def longest_substring_without_repeat_2(s: str):
    seen = set()
    start = 0
    max_value = 0

    for i in range(len(s)):
        element = s[i]

        while element in seen:
            seen.remove(s[start])
            start += 1

        seen.add(element)
        max_value = max(max_value, i - start + 1)
    return max_value


print(longest_substring_without_repeat_2("eghghhgg"))
