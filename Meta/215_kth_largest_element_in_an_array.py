import random

# similar to 347: also quick select
class Solution:
    def findKthLargest(self, nums, k):
        def quick_select(nums, k):
            pivot = random.choice(nums)
            left, mid, right = [], [], []

            for num in nums:
                if num > pivot:
                    left.append(num)
                elif num < pivot:
                    right.append(num)
                else:
                    mid.append(num)

            if k <= len(left):
                return quick_select(left, k)
            elif len(left) + len(mid) < k:
                return quick_select(right, k - len(left) - len(mid))
            else:
                return pivot

        return quick_select(nums, k)

solution = Solution()
print(solution.findKthLargest([5, 5, 6, 4, 3, 3, 2, 1, 2], 4))

# [5, 5, 6, 4, 3, 3, 2, 1, 2] where randomly 3 is chosen to be the pivot...
# k <= len(left): [5, 5, 6, 4]
# else: [3, 3]
# len(left) + len(mid) < k: [2, 1, 2]