# sort by meeting end_time instead of start_time
def non_overlapping_intervals(intervals):
    if not intervals:
        return 0

    # sort by meeting end_time
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 1
    for i in range(1, len(intervals)):
        # Non-overlapping interval found
        if intervals[i][0] >= end:
            end = intervals[i][1]
            count += 1
    return len(intervals) - count

