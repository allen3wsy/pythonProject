class Solution:

    @staticmethod
    def three_sum(nums: list[int]):
      nums.sort()
      result = []
      for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
          continue
        left = i + 1
        right = len(nums) - 1
        while left < right:
          total = nums[i] + nums[left] + nums[right]
          if total < 0:
            left += 1
          elif total > 0:
            right -= 1
          else: # note that there are 2 occurrences of "left += 1" and "right -= 1"
            result.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
              left += 1
            while left < right and nums[right] == nums[right - 1]:
              right -= 1
            left += 1
            right -= 1
      return result

print(Solution.three_sum([-1, 0, 1, 2, -1, -4]))