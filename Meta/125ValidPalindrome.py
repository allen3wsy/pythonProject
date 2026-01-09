class Solution:
    # O(N) complexity and O(1) space
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1
        s = s.lower()
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i] != s[j]:
                return False

            i += 1
            j -= 1
        return True

    # option 2:
    # O(N) complexity and O(N) space: another string to hold the reversed str
    # a bit less ideal
    # def isPalindrome(self, s: str) -> bool:

    #     filtered_chars = filter(lambda ch: ch.isalnum(), s)
    #     lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

    #     filtered_chars_list = list(lowercase_filtered_chars)
    #     reversed_chars_list = filtered_chars_list[::-1]

    #     return filtered_chars_list == reversed_chars_list

solution = Solution()
print(solution.isPalindrome("12 1 "))