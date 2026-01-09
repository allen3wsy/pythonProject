class Solution:
    @staticmethod
    def can_attend_meetings(intervals: list[list[int]]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True


meetings = [[1, 5], [5, 9], [10, 12]]
meetings_2 = [[1, 5], [4, 9], [10, 12]]

print(Solution.can_attend_meetings(meetings))
print(Solution.can_attend_meetings(meetings_2))
