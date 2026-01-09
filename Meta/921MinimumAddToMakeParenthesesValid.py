class Solution:
    #  O(n) - Time O(1)
    def minAddToMakeValid(self, s: str) -> int:
        open_brackets = 0
        min_adds_required = 0

        for c in s:
            if c == "(":
                open_brackets += 1
            elif open_brackets > 0:
                open_brackets -= 1
            else: # if there is not '(' to the left of ')'
                min_adds_required += 1

        # Add the remaining open brackets as closing brackets would be required.
        return min_adds_required + open_brackets

# solution = Solution()
# print(solution.minAddToMakeValid("()"))
# print(solution.minAddToMakeValid("))(("))