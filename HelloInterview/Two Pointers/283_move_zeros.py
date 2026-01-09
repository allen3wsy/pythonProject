class Solution:
    @staticmethod
    def move_zeroes(nums):
        next_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[next_non_zero], nums[i] = nums[i], nums[next_non_zero]
                next_non_zero += 1


array = [0, 1, 0, 3, 2, 4, 0, 1]
Solution.move_zeroes(array)

print(array)
