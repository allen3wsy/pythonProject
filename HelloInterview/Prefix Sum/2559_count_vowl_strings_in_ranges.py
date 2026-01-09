# Leetcode solution is only 1 line different
#
# both problems are super similar
# https://www.hellointerview.com/learn/code/prefix-sum/count-vowels
# Leetcode solution:
def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    ans = [0] * len(queries)
    # building a set, same as: vowels = set(["a", "e", "i", "o", "u"])
    vowels = {"a", "e", "i", "o", "u"}
    prefix_sum = [0] * len(words)
    sum = 0
    for i in range(len(words)):
        current_word = words[i]
        if (current_word[0] in vowels) and (current_word[len(current_word) - 1] in vowels):
            sum += 1
        prefix_sum[i] = sum

    for i in range(len(queries)):
        current_query = queries[i]
        ans[i] = prefix_sum[current_query[1]] - (
            0 if current_query[0] == 0 else prefix_sum[current_query[0] - 1]
        )

    return ans
