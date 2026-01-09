class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1

        # And move p backward through the array, each time writing
        # the largest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            # p2 >= 0 for cases below
            elif p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else: # (p1 < 0) or (p1 >= 0 and nums1[p1] < nums2[p2])
                nums1[p] = nums2[p2]
                p2 -= 1

solution = Solution()
nums1 = [8, 9, 10, 0, 0, 0]
nums2 = [1, 2, 100]

print(nums1)
print(nums2)
solution.merge(nums1, 3, nums2, 3)
print(nums1)