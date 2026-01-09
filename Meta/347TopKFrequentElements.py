
from collections import Counter
import heapq
import random

# similar to 215: also quick select
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        unique_keys = list(count.keys())

        print("unique list: ", unique_keys)

        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique_keys[pivot_index]]
            # 1. Move the pivot to end
            unique_keys[pivot_index], unique_keys[right] = unique_keys[right], unique_keys[pivot_index]

            # 2. Move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique_keys[i]] < pivot_frequency:
                    unique_keys[store_index], unique_keys[i] = unique_keys[i], unique_keys[store_index]
                    store_index += 1

            # 3. Move the pivot to its final place
            unique_keys[right], unique_keys[store_index] = unique_keys[store_index], unique_keys[right]

            return store_index

        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place.
            """
            # base case: the list contains only one element
            if left == right:
                return

            # Select a random pivot_index
            pivot_index = random.randint(left, right)

            # Find the pivot position in a sorted list
            pivot_index = partition(left, right, pivot_index)

            # If the pivot is in its final sorted position
            if k_smallest == pivot_index:
                return
                # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        n = len(unique_keys)
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array.
        # All elements on the left are less frequent.
        # All the elements on the right are more frequent.
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique_keys[n - k:]


    # Solution 2: not the best
    # N log(k) time
    def topKFrequent_2(self, nums: list[int], k: int) -> list[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)

        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)

solution = Solution()
print(solution.topKFrequent([1, 3, 8, 0, 3, 8], 2))
print(solution.topKFrequent_2([1, 3, 8, 0, 3, 8], 3))
