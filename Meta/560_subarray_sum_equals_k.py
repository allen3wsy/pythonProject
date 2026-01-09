# subarray : contiguous non-empty
# this is a array version of path sum III
# brute force check every possibility O(n2), Space O(1)
# Optimal solution:
# with sum frequency map:
# Time O(N), Space O(N)
from collections import defaultdict


# Prefix Sum
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # map = {0: 1} not as good
        # {0: 1} meaning there is 1 case that sum equals 0
        map = defaultdict(int, {0: 1})
        cur_sum = 0
        count = 0
        for n in nums:
            cur_sum += n
            count += map.get(cur_sum - k, 0)
            # map[cur_sum] = map.get(cur_sum, 0) + 1... not as elegant
            map[cur_sum] += 1
        return count

solution = Solution()
print(solution.subarraySum([1, 2, 3], 5))
print(solution.subarraySum([1, 2, 3], 3))