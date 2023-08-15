def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on starting times
    merged_intervals = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged = merged_intervals[-1]

        if current_interval[0] <= last_merged[1]:  # Overlapping intervals
            merged_intervals[-1] = [last_merged[0], max(last_merged[1], current_interval[1])]
        else:
            merged_intervals.append(current_interval)

    return merged_intervals

# Read input
n = int(input())  # Number of intervals
intervals = []
for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

# Merge intervals
result = merge_intervals(intervals)

# Print output
for interval in result:
    print(interval[0], interval[1])
