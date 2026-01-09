class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1

        # 2 pointer solution since the leftMost(if there is negative num and
        # rightMost(if positive num have the biggest abs() value

        for i in reversed(range(n)):
            if abs(nums[left]) >= abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
        return result

solution = Solution()
print(solution.sortedSquares([-4, -1, 0, 3, 10]))