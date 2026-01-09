class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i in range(len(s)):
            # odd length palindrome
            result += self.countPali(s, i, i)
            # even length palindrome
            result += self.countPali(s, i, i + 1)
        return result

    def countPali(self, s, l, r) -> int:
        result = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
            result += 1
        return result

solution = Solution()
print(solution.countSubstrings("aabc"))
