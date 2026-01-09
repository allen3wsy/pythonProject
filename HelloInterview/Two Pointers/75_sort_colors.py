class Solution:
    def sort_colors(self, nums):
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:
                i += 1


solution = Solution()
colors = [2, 0, 1, 1, 0, 1]
solution.sort_colors(colors)
print(colors)
