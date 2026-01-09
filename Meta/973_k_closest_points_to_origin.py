import heapq


# Max Heap solution: O(N⋅logk)
# space: O(K)
class Solution:

    def k_closest(self, points: list[list[int]], k: int) -> list[list[int]]:

        def squared_distance(point: list[int]) -> int:
            """Calculate and return the squared Euclidean distance."""
            return point[0] ** 2 + point[1] ** 2

        # Since heap is sorted in increasing order,
        # negate the distance to simulate max heap
        # and fill the heap with the first k elements of points

        # NOTE: either tuple (_, _) inside heap
        # OR: [_, _] inside heap, but have to keep consistent !!!
        heap = [[-squared_distance(points[i]), i] for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            dist = -squared_distance(points[i])
            if dist > heap[0][0]:
                # If this point is closer than the kth farthest,
                # discard the farthest point and add this one
                heapq.heappushpop(heap, [dist, i])
                # same as the following 2 lines together:
                # heapq.heappop(heap)
                # heapq.heappush(heap, (dist, i))

        # Return all points stored in the max heap
        return [points[i] for [_, i] in heap]


solution = Solution()
print(solution.k_closest([[1, 2], [10, 10], [5, 5]], 1))
print(solution.k_closest([[1, 2], [10, 10], [5, 5]], 2))
print(solution.k_closest([[1, 2], [10, 10], [5, 5]], 3))
