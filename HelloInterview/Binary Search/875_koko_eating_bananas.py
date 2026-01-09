class Solution:
    # Binary search on harvest rate: find minimum rate to finish in h hours
    # Final time: O(log (M *N ))
    # N is the length of apples list
    # M is the max value of the apples list: max(apples)
    @staticmethod
    def min_harvest_rate(apples, h):

        # given a rate, find the total time taken: O(N)
        def time_taken(rate):
            time = 0
            # Calculate total time needed at this harvest rate
            for i in range(len(apples)):
                if apples[i] % rate == 0:
                    time += apples[i] / rate
                else:
                    time += (apples[i] // rate + 1)
            return time

        # Binary search bounds: minimum rate = 1, maximum rate = max apples
        left, right = 1, max(apples)

        # Binary search for minimum valid harvest rate
        while left < right:
            mid = (left + right) // 2
            if time_taken(mid) > h:
                # Rate too slow, need faster rate
                left = mid + 1
            else:
                # Rate is sufficient, try slower rate
                right = mid

        return left

# original array doesn't need to be sorted. I sort it here just easier to understand
apples = [3, 8, 9, 23, 25]
h = 5
print(Solution.min_harvest_rate(apples, h))
