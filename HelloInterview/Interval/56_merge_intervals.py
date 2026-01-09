def merge_intervals(intervals):

    # intervals.sort(key=lambda x: x[0])
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = []

    for interval in sorted_intervals:
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])
    return merged


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals))
