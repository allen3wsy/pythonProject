class Solution:
    # Time: O(N)  Space: O(1): 26
    def can_construct(self, s: str, k: int) -> bool:
        # Handle edge cases
        if len(s) < k:
            return False
        if len(s) == k:
            return True
        # Initialize frequency dictionary and odd_count
        freq = [0] * 26 # O(26) constant space
        odd_count = 0

        # Increment the value of the index corresponding to the current character
        for char in s:
            freq[ord(char) - ord('a')] += 1
        # Count the number of characters that appear an odd number of times in s
        for count in freq:
            if count % 2 == 1:
                odd_count += 1
        # Return if the number of odd frequencies is less than or equal to k
        # EX: not odd_count == k.... it should be:
        return odd_count <= k

    # Option 2: Simpler bit manipulation
    # def can_construct_2(self, s: str, k: int) -> bool:
    #     # Handle edge cases
    #     if len(s) < k:
    #         return False
    #     if len(s) == k:
    #         return True
    #     # Initialize oddCount as an integer bitmask
    #     odd_count = 0

    #     # Update the bitmask for each character in the string
    #     for char in s:
    #         odd_count ^= 1 << (ord(char) - ord("a"))
    #     # Return if the number of odd frequencies is less than or equal to
    #     return bin(odd_count).count('1') <= k

    # For solution 2, remember
    # <<
    # ^=
    # bin(5): returns the binary string -> 0b101
    # bin(5).count('1'): count the occurrences of '1' in the binary string "0b101" -> 2

solution = Solution()
print(solution.can_construct("aabc", 2))
print(solution.can_construct("leetcode", 5))
print(solution.can_construct("leetcode", 6))
