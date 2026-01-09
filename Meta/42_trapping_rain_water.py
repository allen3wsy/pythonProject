class Solution:
    def trap(self, heights: list[int]) -> int:
        if not heights:
            return 0
        left, right = 0, len(heights) - 1
        left_max, right_max = heights[left], heights[right]
        count = 0

        # also works for array size: 2. So that we don't have to check len(heights) >= 3
        # make sure when len() <= 2 the result is 0
        while left < right:
            if left_max < right_max:
                left += 1
                if heights[left] >= left_max:
                    left_max = heights[left]
                else:
                    count += left_max - heights[left]
            else:  # left_max >= right_max:
                right -= 1
                if heights[right] >= right_max:
                    right_max = heights[right]
                else:
                    count += right_max - heights[right]
        return count


solution = Solution()
heights = [4, 2, 0, 3, 2, 5]
print(solution.trap(heights))
