class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i

        return []


solution = Solution()
print(solution.twoSum([1, 2, 3], 5))
print(solution.twoSum([1, 2, 4, 4], 8))


