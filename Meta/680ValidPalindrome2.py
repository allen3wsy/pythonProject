class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Have to define this within "validPalindrome" and before everything else
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                # Found a mismatched pair - try both deletions
                return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)
            i += 1
            j -= 1
        return True

# solution = Solution()
# print(solution.validPalindrome("123"))
# print(solution.validPalindrome("122"))