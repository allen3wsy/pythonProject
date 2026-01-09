# sliding window (variable length)

def character_replacement(s, k):
    state = {}
    max_freq = 0
    max_length = 0
    start = 0

    for end in range(len(s)):
        # state[s[end]] += 1 also works
        # we don't care about len(state) here so we don't have to del state[s[xxx]]
        state[s[end]] = state.get(s[end], 0) + 1
        max_freq = max(max_freq, state[s[end]])

        # max_freq doesn't need to update when we do this since we only care about the
        # biggest max_freq
        if k + max_freq < end - start + 1:
            state[s[start]] -= 1
            start += 1
        max_length = max(max_length, end - start + 1)
    return max_length

print(character_replacement("AABCKL", 2))
print(character_replacement("BCBABCCCCA", 2)) # 4 consecutive C and + (k) = 6