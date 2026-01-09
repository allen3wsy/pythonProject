def employee_free_time(schedule):
    flattened = [i for employee in schedule for i in employee]
    intervals = sorted(flattened, key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    free_times = []
    for i in range(1, len(merged)):
        start = merged[i - 1][1]
        end = merged[i][0]
        free_times.append([start, end])
    return free_times


schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
# merged: [1, 3], [4, 10]
print(employee_free_time(schedule))
