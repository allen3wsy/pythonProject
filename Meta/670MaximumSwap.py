class Solution:
    # @staticmethod
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        n = len(num_str)
        # it means the index of the maximum digit that's not at the leftmost optimal positions
        rightmost_max_index = -1
        swap_idx_1 = -1 # smaller bit
        swap_idx_2 = -1 # larger bit

        # Traverse the string from right to left, tracking the max digit and
        # potential swap
        # range(n - 1, -1, -1))
        for i in reversed(range(n)):
            if rightmost_max_index == -1 or num_str[i] > num_str[rightmost_max_index]:
                rightmost_max_index = i  # Update the index of the max digit
            elif num_str[i] < num_str[rightmost_max_index]:
                swap_idx_1 = i  # Mark the smaller digit for swapping
                # Mark the larger digit for swapping
                swap_idx_2 = rightmost_max_index

        # Perform the swap if a valid swap is found
        if swap_idx_1 != -1 and swap_idx_2 != -1:
            num_str[swap_idx_1], num_str[swap_idx_2] = num_str[swap_idx_2], num_str[swap_idx_1]

        return int("".join(num_str))

solution = Solution()

print(solution.maximumSwap(9812))
print(solution.maximumSwap(1993))