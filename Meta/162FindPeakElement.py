class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1  # Fix right bound

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[mid + 1]:  # Peak is on the left side
                right = mid  # Keep mid because it might be a peak
            else:  # Peak is on the right side
                left = mid + 1  # Move right to explore

        return left  # Left and right converge to the peak index

# there might be more than 1 peaks but this algo guarantees one peak to be found
solution = Solution()

print(solution.findPeakElement([1, 2, 3, 1, 5, 4, 9]))