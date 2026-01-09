class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # i is on abbr: str; count is on word: str
        count, i = 0, 0

        # don't use for i in len(abbr) since we might wanna check digits in abbr
        while i < len(abbr):
            # Check for invalid cases: leading zeros or count overflow
            if abbr[i] == '0' or count >= len(word):
                return False
            # Handle numbers
            numStr = ''
            while i < len(abbr) and abbr[i].isdigit():
                numStr += abbr[i]
                i += 1
            # Update count based on number or letter
            if numStr:
                count += int(numStr)
            elif abbr[i] != word[count]:
                return False
            else:
                count += 1
                i += 1
        return count == len(word)

solution = Solution()
print(solution.validWordAbbreviation("abcd", "a2d"))
print(solution.validWordAbbreviation("internationalization", "i12iz4n"))

# follow up:
# both abbr1 and abbr2 are pattern, return True or False

# A string can be abbreviated by replacing any number of no n -adjacent, no n -empty substrings with their lengths.
# The lengths should not have leading zeros.
# For example, a string such as "substitution" could be abbreviated as (but not limited to):
#
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)
# The following are not valid abbreviations:
#
# "s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
# "s010n" (has leading zeros)
# "s0ubstitution" (replaces an empty substring)
# Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
#
# A substring is a contiguous no n -empty sequence of characters within a string.
#
# Example 1:
#
# Input: word = "internationalization", abbr = "i12iz4n"
# Output: true
# Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").
# Example 2:
#
# Input: word = "apple", abbr = "a2e"
# Output: false
# Explanation: The word "apple" cannot be abbreviated as "a2e".