def insert_intervals(intervals: list[list[int]], new_interval: list[int]):
    merged = []
    i = 0
    n = len(intervals)
    # stage 1: no overlap
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1
    # stage 2: overlapping
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(intervals[i][0], new_interval[0])
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
    merged.append(new_interval)
    # stage 3: no overlap
    while i < n:
        merged.append(intervals[i])
        i += 1
    return merged


intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]

print(insert_intervals(intervals, new_interval))
