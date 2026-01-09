class Solution:
    # Brute force: O(log N)
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            pivot = (left + right) // 2
            # If number of positive integers
            # which are missing before arr[pivot]
            # is less than k -->
            # continue to search on the right.
            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            # Otherwise, go left.
            else:
                right = pivot - 1

        # At the end of the loop, left = right + 1,
        # and the kth missing is in-between arr[right] and arr[left].
        # The number of integers missing before arr[right] is
        # arr[right] - right - 1 -->
        # the number to return is
        # arr[right] + k - (arr[right] - right - 1) = k + left
        return left + k

    # Brute force: O(N)
    def findKthPositive_2(self, arr: list[int], k: int) -> int:
        for num in arr:
            if num <= k:
                k += 1
            elif num > k:
                break
        return k

solution = Solution()

# Strictly increasing positive array: so no duplicates at all !!!
nums = [2, 3, 4, 7, 11]
print(solution.findKthPositive(nums, 3))
print(solution.findKthPositive_2(nums, 3))