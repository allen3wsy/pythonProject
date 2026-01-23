class Solution:
    # binary search: N(log N)
    def find_kth_positive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left. Even if arr[pivot] - pivot - 1 == k, we still look at whole left part !!!
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left = right + 1 + k
        return right + 1 + k  # = left + k

    # Brute force: O(N)
    def find_kth_positive_2(self, arr: list[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            elif num > k:
                break
        return k

solution = Solution()

# Strictly increasing positive array: so no duplicates at all !!!
nums = [2, 3, 4, 7, 11]
print(solution.find_kth_positive(nums, 3))
print(solution.find_kth_positive_2(nums, 3))