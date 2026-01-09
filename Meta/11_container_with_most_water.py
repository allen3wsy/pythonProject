from typing import List

from sorting import sorted_list

class Solution:
    def max_area(self, heights: List[int]) -> int:
        # Your code goes here
        l = 0
        r = len(heights) - 1
        max_area = 0

        while l < r:
            width = r - l
            h = min(heights[l], heights[r])
            current_area = width * h
            max_area = max(max_area, current_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area

solution = Solution()
print(solution.max_area([1,8,6,2,5,4,8,3,7]))
print(solution.max_area([1, 2, 1]))